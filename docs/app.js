// Generic AI prototype runtime — proxy-only. API keys NEVER live in the browser.
// Set window.PROXY_BASE on a per-page basis to point at the deployed Cloudflare Worker.
(function(){
  // PROXY_BASE is set in index.html via <script>window.PROXY_BASE='https://ai-proxy.<sub>.workers.dev/v1'</script>
  // If null/empty, all AI calls return mock.
  function proxyBase(){ return (window.PROXY_BASE || '').replace(/\/$/,''); }
  function hasProxy(){ return !!proxyBase(); }

  const banner = (msg, ok=false) => {
    const el = document.getElementById('ai-banner');
    if (!el) return;
    el.textContent = msg;
    el.className = 'banner' + (ok ? ' banner-ok' : '');
    el.style.display = 'block';
  };

  async function tryAnthropic(userPrompt, systemPrompt) {
    if (!hasProxy()) return { mocked:true, reason:'PROXY_BASE not configured — set window.PROXY_BASE to the deployed Worker URL' };
    try {
      const res = await fetch(`${proxyBase()}/anthropic/messages`, {
        method:'POST',
        headers:{ 'content-type':'application/json' },
        body: JSON.stringify({
          model:'claude-sonnet-4-5-20250929',
          max_tokens:512,
          system: systemPrompt,
          messages:[{role:'user',content:userPrompt}]
        })
      });
      if (!res.ok) {
        const t = await res.text();
        return { mocked:true, reason:`Proxy ${res.status}: ${t.slice(0,120)}` };
      }
      const j = await res.json();
      return { mocked:false, text: (j.content||[]).map(c=>c.text).join('\n') };
    } catch (e) {
      return { mocked:true, reason:'Network: '+e.message };
    }
  }

  async function tryGemini(userPrompt, systemPrompt, model='gemini-2.0-flash') {
    if (!hasProxy()) return { mocked:true, reason:'PROXY_BASE not configured' };
    try {
      const res = await fetch(`${proxyBase()}/gemini/v1/models/${model}:generateContent`, {
        method:'POST',
        headers:{ 'content-type':'application/json' },
        body: JSON.stringify({
          system_instruction: systemPrompt ? { parts:[{text:systemPrompt}] } : undefined,
          contents:[{role:'user',parts:[{text:userPrompt}]}]
        })
      });
      if (!res.ok) {
        const t = await res.text();
        return { mocked:true, reason:`Proxy ${res.status}: ${t.slice(0,120)}` };
      }
      const j = await res.json();
      const text = (j.candidates?.[0]?.content?.parts || []).map(p=>p.text).join('\n');
      return { mocked:false, text };
    } catch (e) { return { mocked:true, reason:'Network: '+e.message }; }
  }

  // Theme handling
  function initTheme(){
    const saved = localStorage.getItem('theme');
    if (saved) document.documentElement.setAttribute('data-theme', saved);
    const btn = document.getElementById('theme-toggle');
    if (btn) {
      const sync = () => {
        const cur = document.documentElement.getAttribute('data-theme') ||
          (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark':'light');
        btn.textContent = cur === 'dark' ? '☀ Light' : '☾ Dark';
      };
      btn.addEventListener('click', () => {
        const cur = document.documentElement.getAttribute('data-theme') ||
          (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark':'light');
        const next = cur === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        sync();
      });
      sync();
    }
  }

  // Show live/mock status on load
  function showStatus(){
    if (hasProxy()) banner('Live AI via proxy: ' + proxyBase(), true);
    else banner('Mock mode — proxy not configured. AI buttons return mock data.', false);
  }

  window.app = {
    // hasKey kept for backward compat — now answers "is proxy configured"
    hasKey: () => hasProxy(),
    banner,
    tryAnthropic,
    tryGemini,
    setKey() {
      banner('🔒 Keys live on the Cloudflare Worker, never in the browser. Set them via CF dashboard → Worker → Variables.', false);
    },
    loadMock(url){ return fetch(url).then(r=>r.json()); }
  };
  document.addEventListener('DOMContentLoaded', () => { initTheme(); showStatus(); });
})();
