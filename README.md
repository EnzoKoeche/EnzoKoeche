<p align="center">
  <img src="./assets/banner.svg" alt="Enzo Koeche — Software Engineer · Applied AI" width="100%">
</p>

I build systems that think — AI agents, data platforms and web products that hold up in production.

Right now: **Applied AI @ [Lyx Engenharia](https://lyx.com.br)**, building internal systems for one of
southern Brazil's largest homebuilders, and **[Milkup](https://milkup.com.br)**, software for dairy
companies. Software Engineering at PUCPR, in Curitiba.

<a href="https://enzokoeche.vercel.app"><img src="https://img.shields.io/badge/Portfolio-enzokoeche.vercel.app-0D1513?style=flat-square&logo=vercel&logoColor=00E5C0&labelColor=0A0F0E"></a>
<a href="https://www.linkedin.com/in/enzo-koeche-castagna-82ab6137b/"><img src="https://img.shields.io/badge/LinkedIn-Enzo%20Koeche-0D1513?style=flat-square&labelColor=0A0F0E"></a>
<a href="mailto:koechecastagnaenzo@gmail.com"><img src="https://img.shields.io/badge/Email-koechecastagnaenzo-0D1513?style=flat-square&logo=gmail&logoColor=00E5C0&labelColor=0A0F0E"></a>

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

![Python](https://img.shields.io/badge/Python-0D1513?style=flat-square&logo=python&logoColor=00E5C0)
![TypeScript](https://img.shields.io/badge/TypeScript-0D1513?style=flat-square&logo=typescript&logoColor=00E5C0)
![JavaScript](https://img.shields.io/badge/JavaScript-0D1513?style=flat-square&logo=javascript&logoColor=00E5C0)
![SQL](https://img.shields.io/badge/SQL-0D1513?style=flat-square&logo=postgresql&logoColor=00E5C0)
![C#](https://img.shields.io/badge/C%23-0D1513?style=flat-square&logo=dotnet&logoColor=00E5C0)
![Dart](https://img.shields.io/badge/Dart-0D1513?style=flat-square&logo=dart&logoColor=00E5C0)

**AI & Data**

![LangGraph](https://img.shields.io/badge/LangGraph-0D1513?style=flat-square&logo=langchain&logoColor=00E5C0)
![LangChain](https://img.shields.io/badge/LangChain-0D1513?style=flat-square&logo=langchain&logoColor=00E5C0)
![Anthropic](https://img.shields.io/badge/Anthropic%20SDK-0D1513?style=flat-square&logo=anthropic&logoColor=00E5C0)
![OpenAI](https://img.shields.io/badge/OpenAI%20SDK-0D1513?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-0D1513?style=flat-square&logo=pandas&logoColor=00E5C0)
![Power BI](https://img.shields.io/badge/Power%20BI-0D1513?style=flat-square)

**Web & Backend**

![Next.js](https://img.shields.io/badge/Next.js-0D1513?style=flat-square&logo=nextdotjs&logoColor=00E5C0)
![React](https://img.shields.io/badge/React-0D1513?style=flat-square&logo=react&logoColor=00E5C0)
![Tailwind](https://img.shields.io/badge/Tailwind-0D1513?style=flat-square&logo=tailwindcss&logoColor=00E5C0)
![Node.js](https://img.shields.io/badge/Node.js-0D1513?style=flat-square&logo=nodedotjs&logoColor=00E5C0)
![FastAPI](https://img.shields.io/badge/FastAPI-0D1513?style=flat-square&logo=fastapi&logoColor=00E5C0)
![Streamlit](https://img.shields.io/badge/Streamlit-0D1513?style=flat-square&logo=streamlit&logoColor=00E5C0)

**Data & Infra**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0D1513?style=flat-square&logo=postgresql&logoColor=00E5C0)
![Supabase](https://img.shields.io/badge/Supabase-0D1513?style=flat-square&logo=supabase&logoColor=00E5C0)
![Prisma](https://img.shields.io/badge/Prisma-0D1513?style=flat-square&logo=prisma&logoColor=00E5C0)
![Docker](https://img.shields.io/badge/Docker-0D1513?style=flat-square&logo=docker&logoColor=00E5C0)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-0D1513?style=flat-square&logo=githubactions&logoColor=00E5C0)
![Vercel](https://img.shields.io/badge/Vercel-0D1513?style=flat-square&logo=vercel&logoColor=00E5C0)

**Mobile & Desktop**

![Flutter](https://img.shields.io/badge/Flutter-0D1513?style=flat-square&logo=flutter&logoColor=00E5C0)
![.NET](https://img.shields.io/badge/.NET%208-0D1513?style=flat-square&logo=dotnet&logoColor=00E5C0)
![SQLite](https://img.shields.io/badge/SQLite-0D1513?style=flat-square&logo=sqlite&logoColor=00E5C0)

---

## Stats

<img src="./assets/stats.svg" alt="Public repos, commits, contributions and language split" width="100%">

---

<sub>The two images above aren't widgets. The banner is drawn from a fixed seed by
<a href="scripts/gen_banner.py"><code>gen_banner.py</code></a>, and the stats card is redrawn every Monday
from the GitHub API by <a href="scripts/gen_stats.py"><code>gen_stats.py</code></a> and committed here —
the hosted card service was returning 503, and a broken image on a profile is worse than no card.</sub>
