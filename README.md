<p align="center">
  <img src="./assets/banner.svg" alt="Enzo Koeche — Software Engineer · Applied AI" width="100%">
</p>

I build systems that think — AI agents, data platforms and web products that hold up in production.

Right now: **Applied AI @ [Lyx Engenharia](https://lyx.com.br)**, building internal systems for one of
southern Brazil's largest homebuilders, and **[Milkup](https://milkup.com.br)**, software for dairy
companies. Software Engineering at PUCPR, in Curitiba.

> **New:** my portfolio now runs a retrieval agent **in your browser** — ask it anything about me, it answers with a cited source or an honest *"I didn't find it"*. No server, no API key, your question never leaves the page. → **[enzokoeche.vercel.app/#perguntar](https://enzokoeche.vercel.app/#perguntar)**

<a href="https://enzokoeche.vercel.app"><img src="https://img.shields.io/badge/Portfolio-enzokoeche.vercel.app-0A1B38?style=flat-square&logo=vercel&logoColor=FF7A1A&labelColor=071228"></a>
<a href="https://www.linkedin.com/in/enzo-koeche-castagna-82ab6137b/"><img src="https://img.shields.io/badge/LinkedIn-Enzo%20Koeche-0A1B38?style=flat-square&labelColor=071228"></a>
<a href="mailto:koechecastagnaenzo@gmail.com"><img src="https://img.shields.io/badge/Email-koechecastagnaenzo-0A1B38?style=flat-square&logo=gmail&logoColor=FF7A1A&labelColor=071228"></a>

---

## How I work

Five things I insist on. Each one has public code proving it isn't just talk.

| | |
|---|---|
| **A system that doesn't know must say so** | Hallucination isn't a model bug, it's an architecture decision. With no retrieved basis, the right answer is *"I didn't find it"* — enforced with a test, not a prompt. → [`rag-conformidade-laticinios`](https://github.com/EnzoKoeche/rag-conformidade-laticinios) |
| **AI supports the decision; a person makes it** | In credit, health or compliance, automating judgement hands responsibility to something that can't carry it. I build with an explicit interrupt for human approval. → [`agente-credito-langgraph`](https://github.com/EnzoKoeche/agente-credito-langgraph) |
| **If you can't measure it, it isn't done** | *"Seems better"* is not a result. Deterministic evals in CI, cost and latency tracked, coverage where the logic is critical. A number nobody verifies is decoration. |
| **Every change needs a way back** | Migration, registry tweak, deploy: if it can't be undone, it isn't done. Nobody gives you a second chance after you break their machine. → [`fpsbooster`](https://github.com/EnzoKoeche/fpsbooster) |
| **Sensitive data doesn't get in without a plan** | Portfolio projects run on synthetic data, and PII in production is handled explicitly — not as a detail to sort out later. A leak has no rollback. |

---

## Selected work

| Project | What it is | Built with |
|---|---|---|
| **[RAG Conformidade Laticínios](https://github.com/EnzoKoeche/rag-conformidade-laticinios)** | Agentic RAG answering dairy-compliance questions with a cited official source — or an honest *"I don't know"*. | `Python` `LangGraph` `RAG` `Streamlit` |
| **[enzokoeche-site](https://github.com/EnzoKoeche/enzokoeche-site)** | This profile's big brother: an engineering sheet with live GitHub telemetry, an in-browser BM25 agent (eval-enforced refusal) and the build's commit printed on the title block. | `Next.js` `TypeScript` `BM25` |
| **[Agente de Crédito](https://github.com/EnzoKoeche/agente-credito-langgraph)** | Consumer-credit analysis agent with typed state, human-in-the-loop and evals that run in CI. | `Python` `LangGraph` `HITL` `Evals` |
| **[ShadowMesh](https://github.com/EnzoKoeche/shadowmesh)** | An AI security control plane: discovers, classifies and governs AI tool usage across an organisation. | `Python` `Security` `Governance` |
| **[Soulstone](https://github.com/EnzoKoeche/soulstone)** | Real-time Steam Market price tracker for the *TBH: Task Bar Hero* community. | `React` `TypeScript` `Supabase` |
| **[Orkestree](https://github.com/EnzoKoeche/Orkestree)** | Web platform with technical docs versioned alongside the code and an external brain in Notion. | `Next.js` `PostgreSQL` `Prisma` |
| **[FPSBooster](https://github.com/EnzoKoeche/fpsbooster)** | FPS and latency optimiser for Windows: detects hardware, suggests tweaks, applies them reversibly. | `C#` `.NET 8` `WPF` |

More, with write-ups → **[enzokoeche.vercel.app](https://enzokoeche.vercel.app)**

---

## Stack

Tools I use often enough to have opinions about.

**Languages**

![Python](https://img.shields.io/badge/Python-0A1B38?style=flat-square&logo=python&logoColor=FF7A1A)
![TypeScript](https://img.shields.io/badge/TypeScript-0A1B38?style=flat-square&logo=typescript&logoColor=FF7A1A)
![JavaScript](https://img.shields.io/badge/JavaScript-0A1B38?style=flat-square&logo=javascript&logoColor=FF7A1A)
![SQL](https://img.shields.io/badge/SQL-0A1B38?style=flat-square&logo=postgresql&logoColor=FF7A1A)
![C#](https://img.shields.io/badge/C%23-0A1B38?style=flat-square&logo=dotnet&logoColor=FF7A1A)
![Dart](https://img.shields.io/badge/Dart-0A1B38?style=flat-square&logo=dart&logoColor=FF7A1A)

**AI & Data**

![LangGraph](https://img.shields.io/badge/LangGraph-0A1B38?style=flat-square&logo=langchain&logoColor=FF7A1A)
![LangChain](https://img.shields.io/badge/LangChain-0A1B38?style=flat-square&logo=langchain&logoColor=FF7A1A)
![Anthropic](https://img.shields.io/badge/Anthropic%20SDK-0A1B38?style=flat-square&logo=anthropic&logoColor=FF7A1A)
![OpenAI](https://img.shields.io/badge/OpenAI%20SDK-0A1B38?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-0A1B38?style=flat-square&logo=pandas&logoColor=FF7A1A)
![Power BI](https://img.shields.io/badge/Power%20BI-0A1B38?style=flat-square)

**Web & Backend**

![Next.js](https://img.shields.io/badge/Next.js-0A1B38?style=flat-square&logo=nextdotjs&logoColor=FF7A1A)
![React](https://img.shields.io/badge/React-0A1B38?style=flat-square&logo=react&logoColor=FF7A1A)
![Tailwind](https://img.shields.io/badge/Tailwind-0A1B38?style=flat-square&logo=tailwindcss&logoColor=FF7A1A)
![Node.js](https://img.shields.io/badge/Node.js-0A1B38?style=flat-square&logo=nodedotjs&logoColor=FF7A1A)
![FastAPI](https://img.shields.io/badge/FastAPI-0A1B38?style=flat-square&logo=fastapi&logoColor=FF7A1A)
![Streamlit](https://img.shields.io/badge/Streamlit-0A1B38?style=flat-square&logo=streamlit&logoColor=FF7A1A)

**Data & Infra**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0A1B38?style=flat-square&logo=postgresql&logoColor=FF7A1A)
![Supabase](https://img.shields.io/badge/Supabase-0A1B38?style=flat-square&logo=supabase&logoColor=FF7A1A)
![Prisma](https://img.shields.io/badge/Prisma-0A1B38?style=flat-square&logo=prisma&logoColor=FF7A1A)
![Docker](https://img.shields.io/badge/Docker-0A1B38?style=flat-square&logo=docker&logoColor=FF7A1A)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-0A1B38?style=flat-square&logo=githubactions&logoColor=FF7A1A)
![Vercel](https://img.shields.io/badge/Vercel-0A1B38?style=flat-square&logo=vercel&logoColor=FF7A1A)

**Mobile & Desktop**

![Flutter](https://img.shields.io/badge/Flutter-0A1B38?style=flat-square&logo=flutter&logoColor=FF7A1A)
![.NET](https://img.shields.io/badge/.NET%208-0A1B38?style=flat-square&logo=dotnet&logoColor=FF7A1A)
![SQLite](https://img.shields.io/badge/SQLite-0A1B38?style=flat-square&logo=sqlite&logoColor=FF7A1A)

---

## Stats

<img src="./assets/stats.svg" alt="Public repos, commits, contributions and language split" width="100%">

---

<sub>The two images above aren't widgets. The banner is drawn from a fixed seed by
<a href="scripts/gen_banner.py"><code>gen_banner.py</code></a>, and the stats card is redrawn every Monday
from the GitHub API by <a href="scripts/gen_stats.py"><code>gen_stats.py</code></a> and committed here —
the hosted card service was returning 503, and a broken image on a profile is worse than no card.</sub>
