# Limitations & API Key Requirements

This prototype is **front-end-only with mock data**. Real AI features require API keys and (for most calls) a server-side proxy due to browser CORS.

## API keys (stored in browser localStorage only — never on a server)

Open browser DevTools → Console and run **one** of:

```js
localStorage.setItem('ANTHROPIC_API_KEY', 'sk-ant-...');
localStorage.setItem('OPENAI_API_KEY',    'sk-...');
localStorage.setItem('GEMINI_API_KEY',    'AIza...');
localStorage.setItem('GROK_API_KEY',      'xai-...');
```

Then reload. The "Live AI" badge will appear and supported buttons will attempt real calls.

## CORS reality (2026)
- **Anthropic Messages API** — supports CORS for `anthropic-dangerous-direct-browser-access: true`, but for production you should proxy via your own server.
- **OpenAI / Gemini / Grok** — generally block direct browser calls; need a server proxy or Cloudflare Worker.
- **Whisper / Ollama / vLLM** — local; require a backend you run yourself.

## What's mocked vs real in this prototype
| Capability | Status | Becomes real with |
|---|---|---|
| All forms / mock data | ✅ works locally | — |
| LLM calls | 🔶 mock by default | Anthropic key + browser-direct flag, or proxy |
| Voice (Whisper) | 🔶 Web Speech API fallback | Run Whisper locally |
| Vector RAG | 🔶 mocked | Qdrant / pgvector + embeddings provider |
| Third-party integrations (Stripe, Jira, Square, Twilio, Health Connect) | 🔶 mocked | OAuth setup + server |
| Persistence | 🔶 in-memory only | SQLite / Postgres backend |

## Recommended path to production
1. Front this prototype with a small FastAPI / Cloudflare Worker proxy.
2. Inject API keys server-side; clients never see them.
3. Replace mock data with real persistence.
4. Wire MCP servers for the third-party integrations.
5. Add Promptfoo / Langfuse for eval + observability.

See **`AI_USE_CASES.md`** for the full agentic upgrade plan.
