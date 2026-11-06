<div align="center">

<img src="./assets/banner.svg" alt="Aditya Mishra - Full-Stack Developer & AI Systems Engineer" width="100%" />

<br><br>

<a href="https://portfolio-adiimishraa.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-0d1117?style=for-the-badge&logo=googlechrome&logoColor=38bdf8&color=0d1117" alt="Portfolio" /></a>
&nbsp;
<a href="https://www.linkedin.com/in/adi-mishraa/"><img src="https://img.shields.io/badge/LinkedIn-0d1117?style=for-the-badge&logo=linkedin&logoColor=38bdf8&color=0d1117" alt="LinkedIn" /></a>
&nbsp;
<a href="https://github.com/adimishra-code"><img src="https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=38bdf8&color=0d1117" alt="GitHub" /></a>
&nbsp;
<a href="mailto:adityamishrav820@gmail.com"><img src="https://img.shields.io/badge/Email-0d1117?style=for-the-badge&logo=gmail&logoColor=38bdf8&color=0d1117" alt="Email" /></a>

<br><br>

</div>

---

### Overview

I'm an Information Technology undergraduate at **Gautam Buddha University** and a full-stack developer building robust web applications and autonomous AI agent pipelines. My focus centers on solid system architecture, defensive API design, and deploying resilient backends with real-time capabilities.

<table>
  <tr>
    <td width="33%" align="center">
      <b>Core Focus</b><br>
      <sub>AI Agent Loops · App Security · Systems</sub>
    </td>
    <td width="33%" align="center">
      <b>Primary Stack</b><br>
      <sub>TypeScript · Python · Fastify · React · LangGraph</sub>
    </td>
    <td width="33%" align="center">
      <b>Education</b><br>
      <sub>B.Tech in IT @ Gautam Buddha University</sub>
    </td>
  </tr>
</table>

---

### Featured Systems & Architecture

#### 🛡️ [Extension Guard](https://github.com/adimishra-code/extensionguard) &nbsp;·&nbsp; [Live Scanner](https://extensionguard-web.onrender.com)
*Automated 5-stage security analysis pipeline for Chromium and Firefox extensions.*

```
[ Extension Archive (.zip / .crx) ]
              │
    ┌─────────┴─────────┐
    ▼                   ▼
[ Static AST Analysis ]   [ Sandboxed Dynamic Run (Playwright) ]
    │                   │
    └─────────┬─────────┘
              ▼
  [ LLM Threat Review + Weighted 0–100 Risk Engine ]
```

- **Static & Dynamic Analysis**: Extracts AST nodes from content scripts, parses manifest permissions, and runs the unpacked extension inside an isolated Playwright browser context to detect runtime evasion.
- **Threat Scoring Engine**: Weights high-risk permissions (`webRequestBlocking`, broad host permissions, `debugger`), malicious network callbacks, and script injections into a composite risk grade.
- **Tech**: `TypeScript` · `Fastify` · `React` · `PostgreSQL` · `Redis` · `Playwright` · `Docker`

<br>

#### 🧠 [DocsMind](https://docsmind-beige.vercel.app/) &nbsp;·&nbsp; [Live App](https://docsmind-beige.vercel.app/)
*Document intelligence engine with hybrid dense-sparse retrieval and multi-step reasoning.*

```
[ Document / PDF ] ──> [ OCR & Semantic Chunking ] ──> [ Dense Embeddings + BM25 Lexical ]
                                                                     │
[ Streamed Answer + Citations ] <── [ LangGraph Agent Loop ] <── [ Cross-Encoder Reranker ]
```

- **Hybrid Retrieval**: Combines Qdrant vector similarity with BM25 keyword matching and a cross-encoder reranking pass to eliminate hallucinations on technical documentation.
- **Multi-Step Agent Loop**: Uses LangGraph to orchestrate query decomposition, iterative context retrieval, and token-streamed responses with verified source citations.
- **Tech**: `FastAPI` · `Python` · `React` · `Qdrant` · `Redis` · `LangGraph` · `LangChain`

<br>

#### ⚡ Sentinel *(In Active Development)*
*Multi-tenant AI Trust & Safety platform with configurable moderation engines.*
- **Multilingual Moderation**: Real-time content classification for English, Hindi, and Hinglish using specialized prompting strategies and small-footprint models.
- **Enterprise Controls**: Configurable policy engine, immutable audit trail, automated risk-level routing, and a dedicated queue for human-in-the-loop appeal workflows.
- **Tech**: `Node.js` · `Fastify` · `FastAPI` · `TypeScript` · `React` · `MongoDB` · `Gemini`

<br>

#### 🚗 [CampusPool](https://campuspool.pages.dev/) &nbsp;·&nbsp; [Live Platform](https://campuspool.pages.dev/)
*Peer-to-peer carpooling network designed for university student transit.*
- **Matching & Safety**: Weighted route-matching algorithm pairing student schedules, backed by institutional email verification and in-app SOS safety mechanisms.
- **Real-Time Communication**: WebSocket-driven instant messaging, ride coordination, and live driver location telemetry.
- **Tech**: `React` · `Redux Toolkit` · `Node.js` · `MongoDB` · `Socket.IO` · `Tailwind CSS`

---

### Additional Projects

<details>
<summary><b>Explore More Projects</b></summary>
<br>

- **JARVIS / Chitragupta**: Modular desktop AI assistant featuring a dynamic tool registry, 3-layer persistent memory, voice activation, and permission-gated execution via FastAPI and Ollama.
- **Tally**: Warehouse inventory platform with an append-only transaction ledger, multi-tenant RBAC, and background queue workers for reconciliation.
- **EduPulse Academy & OMBREILLE**: Developed backend integrations and responsive landing systems during internship engagements at Skypath Global.

</details>

---

### Technical Proficiencies

| Area | Technologies |
|:---|:---|
| **Languages** | `TypeScript` `JavaScript` `Python` `SQL` `C` `C++` |
| **Backend & APIs** | `Node.js` `Fastify` `Express` `FastAPI` `RESTful APIs` `WebSockets` |
| **Databases & Cache** | `PostgreSQL` `MongoDB` `Redis` `Qdrant (Vector DB)` |
| **AI & Orchestration** | `LangGraph` `LangChain` `RAG Architectures` `Ollama` `Gemini API` |
| **Frontend** | `React` `Redux Toolkit` `Tailwind CSS` `Vite` `HTML5 / CSS3` |
| **DevOps & Tooling** | `Docker` `Playwright` `Git` `GitHub Actions` `Linux` `Postman` |

---

### Experience & Education

```
2026          Full Stack Developer Intern — Skypath Global
              Contributed full-stack features and API integrations across two client platforms
              (EduPulse Academy and OMBREILLE).

2024 – Present B.Tech in Information Technology — Gautam Buddha University
              Focusing on algorithms, system design, databases, computer networks, and application security.
```

---

### Certifications & Verified Training

- **Walmart Global Tech** — Advanced Software Engineering Job Simulation *(Forage)*
  - Implemented core backend services, architected relational data models, and resolved performance bottlenecks.
- **NxtWave** — Intensive AI Bootcamp Certification *(2026)*
  - Rigorous training in machine learning concepts, prompt architecture, and generative AI agent workflows.
- **Nokia & TSSC Noida** — AI/ML Technical Workshop
  - Hands-on practical modules covering predictive modeling and machine learning applications in telecommunications.
- **IgNITion Techfest, Gautam Buddha University** — Top 25 Finalist, Tech Tank *(2025)* & Hackathon 2.0 Participant *(2026)*
- **Intra-Institutional AI Hackathon** — Organizing Committee Member
