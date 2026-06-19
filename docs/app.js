// Generic AI prototype runtime. Each repo wires its domain UI through window.app callbacks.
(function(){
  const KEYS = { anthropic:'ANTHROPIC_API_KEY', openai:'OPENAI_API_KEY', gemini:'GEMINI_API_KEY', grok:'GROK_API_KEY' };
  const hasKey = (k) => !!localStorage.getItem(KEYS[k] || k);
  const banner = (msg, ok=false) => {
    const el = document.getElementById('ai-banner');
    if (!el) return;
    el.textContent = msg;
    el.className = 'banner' + (ok ? ' banner-ok' : '');
    el.style.display = 'block';
  };
  async function tryAnthropic(userPrompt, systemPrompt) {
    const key = localStorage.getItem('ANTHROPIC_API_KEY');
    if (!key) return { mocked:true, reason:'No ANTHROPIC_API_KEY in localStorage' };
    try {
      const res = await fetch('https://api.anthropic.com/v1/messages', {
        method:'POST',
        headers:{'content-type':'application/json','x-api-key':key,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},
        body: JSON.stringify({ model:'claude-sonnet-4-5-20250929', max_tokens:512, system: systemPrompt, messages:[{role:'user',content:userPrompt}] })
      });
      if (!res.ok) return { mocked:true, reason:`API ${res.status}` };
      const j = await res.json();
      return { mocked:false, text: (j.content||[]).map(c=>c.text).join('\n') };
    } catch (e) { return { mocked:true, reason:'CORS or network: '+e.message }; }
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
  window.app = {
    hasKey, banner, tryAnthropic,
    setKey(provider) {
      const v = prompt(`Paste ${provider} API key (stored only in this browser's localStorage):`);
      if (v) { localStorage.setItem(KEYS[provider]||provider, v); banner(`✓ ${provider} key saved locally`, true); }
    },
    loadMock(url){ return fetch(url).then(r=>r.json()); }
  };
  document.addEventListener('DOMContentLoaded', initTheme);
})();
