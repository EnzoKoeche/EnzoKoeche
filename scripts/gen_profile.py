# -*- coding: utf-8 -*-
"""Gera as imagens do perfil: o terminal do topo e os dois diagramas.

Tudo sai daqui, em dois temas (escuro e claro), sem imagem baixada nem servico
de terceiro. O terminal anima com SMIL, que roda dentro de <img> no GitHub;
quem renderiza sem animacao (rsvg, preview) ve so a moldura, por isso o
STATIC=1 desenha o estado final para conferir.

    python3 scripts/gen_profile.py
    STATIC=1 python3 scripts/gen_profile.py   # sem animacao, para preview
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = f"{RAIZ}/assets"
STATIC = os.environ.get("STATIC") == "1"

MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

TEMAS = {
    "dark": dict(bg="#0a0a0a", panel="#0f0f0f", chip="#151515", ink="#f2f2f2",
                 dim="#8a8a8a", faint="#4d4d4d", line="#ffffff"),
    "light": dict(bg="#fbfbfb", panel="#ffffff", chip="#f2f2f2", ink="#0b0b0b",
                  dim="#5c5c5c", faint="#b0b0b0", line="#000000"),
}


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def salvar(nome, partes):
    caminho = f"{ASSETS}/{nome}"
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("\n".join(partes) + "\n")
    print(caminho)


# ── terminal do topo ────────────────────────────────────────────────────────

FS = 15                # tamanho da fonte do corpo
CW = FS * 0.602        # largura de um caractere em monoespacada (Menlo/SF Mono)
LH = 27                # altura da linha
X0 = 34                # margem esquerda do texto

# (tipo, segmentos). "cmd" e digitado; "out" aparece de uma vez; "gap" e linha vazia.
# estilos: b = negrito na cor da tinta, i = tinta, d = apagado
LINHAS = [
    ("cmd", "whoami"),
    ("out", [("Enzo Koeche", "b"), ("  ·  software engineer  ·  Curitiba, BR", "d")]),
    ("gap", None),
    ("cmd", "cat now.md"),
    ("out", [("Lyx Engenharia", "b"),
             (" — I build and run its internal platform, end to end:", "i")]),
    ("out", [("  backend ", "d"), ("NestJS · Bun · Postgres", "i"),
             ("    data ", "d"), ("Python · Airflow", "i"),
             ("    BI ", "d"), ("Next.js", "i"),
             ("    agents ", "d"), ("Claude Code · MCP", "i")]),
    ("gap", None),
    ("cmd", "gh search prs --author @me --owner Lyx-Engenharia --merged --limit 1000 --json number -q length"),
    ("out", [("670", "b"), ("    merged PRs · 6 repos · since 2026-09", "d")]),
    ("gap", None),
    ("cmd", "cat building.md"),
    ("out", [("Trackside", "b"),
             (" — desktop workbench for AI coding agents. Rust core, Tauri 2, MCP policy gateway.", "i")]),
    ("out", [("  week one: 471 commits · 107 PRs · 61 ADRs  →  tracksidehq.dev", "d")]),
    ("gap", None),
    ("end", None),
]


def terminal(tema):
    t = TEMAS[tema]
    W = 1200
    topo = 44
    y0 = topo + 40
    H = y0 + LH * (len(LINHAS) - 1) + 30

    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="Terminal: Enzo Koeche, software engineer. Building the internal platform '
      f'at Lyx Engenharia end to end; 670 merged PRs since September 2026; building Trackside.">')
    a(f'<rect width="{W}" height="{H}" rx="10" fill="{t["bg"]}"/>')
    a(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="none" '
      f'stroke="{t["line"]}" stroke-opacity="0.14"/>')
    # barra de titulo
    a(f'<line x1="0" y1="{topo}" x2="{W}" y2="{topo}" stroke="{t["line"]}" stroke-opacity="0.10"/>')
    for i in range(3):
        a(f'<circle cx="{24 + i * 20}" cy="{topo / 2}" r="5.5" fill="none" '
          f'stroke="{t["line"]}" stroke-opacity="0.28"/>')
    a(f'<text x="{W / 2}" y="{topo / 2 + 4}" text-anchor="middle" font-family="{MONO}" '
      f'font-size="12" fill="{t["dim"]}">kcz@cwb: ~ — zsh — 132×{len(LINHAS) + 2}</text>')
    a(f'<text x="{W - 24}" y="{topo / 2 + 4}" text-anchor="end" font-family="{MONO}" '
      f'font-size="11" letter-spacing="1.5" fill="{t["faint"]}">UTC−3</text>')

    cor = {"b": t["ink"], "i": t["ink"], "d": t["dim"]}
    peso = {"b": "700", "i": "400", "d": "400"}
    relogio = 0.5
    prompt = "$ "

    for n, (tipo, conteudo) in enumerate(LINHAS):
        y = y0 + n * LH
        if tipo == "gap":
            continue

        if tipo == "cmd":
            inicio = relogio
            dur = min(len(conteudo) * 0.03, 1.5)
            px = X0 + len(prompt) * CW
            a(f'<g opacity="{1 if STATIC else 0}">')
            if not STATIC:
                a(f'<set attributeName="opacity" to="1" begin="{inicio:.2f}s" fill="freeze"/>')
            a(f'<text x="{X0}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{t["dim"]}" '
              f'xml:space="preserve">{prompt}</text>')
            if STATIC:
                a(f'<text x="{px:.1f}" y="{y}" font-family="{MONO}" font-size="{FS}" '
                  f'fill="{t["ink"]}" xml:space="preserve">{esc(conteudo)}</text>')
            else:
                cid = f"c{n}"
                passos = ";".join(f"{i * CW * 1.04:.1f}" for i in range(len(conteudo) + 1))
                a(f'<clipPath id="{cid}"><rect x="{px:.1f}" y="{y - FS - 4}" width="0" height="{FS + 10}">'
                  f'<animate attributeName="width" values="{passos}" calcMode="discrete" '
                  f'begin="{inicio:.2f}s" dur="{dur:.2f}s" fill="freeze"/></rect></clipPath>')
                a(f'<text x="{px:.1f}" y="{y}" font-family="{MONO}" font-size="{FS}" '
                  f'fill="{t["ink"]}" clip-path="url(#{cid})" xml:space="preserve">{esc(conteudo)}</text>')
            a('</g>')
            relogio = inicio + dur + 0.3
            continue

        if tipo == "out":
            spans = "".join(
                f'<tspan fill="{cor[e]}" font-weight="{peso[e]}">{esc(s)}</tspan>' for s, e in conteudo)
            a(f'<text x="{X0}" y="{y}" font-family="{MONO}" font-size="{FS}" xml:space="preserve" '
              f'opacity="{1 if STATIC else 0}">{spans}'
              + ("" if STATIC else
                 f'<set attributeName="opacity" to="1" begin="{relogio:.2f}s" fill="freeze"/>')
              + '</text>')
            relogio += 0.12
            # pausa depois do ultimo "out" de um bloco, como quem le a saida
            prox = LINHAS[n + 1][0] if n + 1 < len(LINHAS) else None
            if prox != "out":
                relogio += 0.45
            continue

        if tipo == "end":
            a(f'<text x="{X0}" y="{y}" font-family="{MONO}" font-size="{FS}" fill="{t["dim"]}" '
              f'xml:space="preserve" opacity="{1 if STATIC else 0}">{prompt}'
              + ("" if STATIC else
                 f'<set attributeName="opacity" to="1" begin="{relogio:.2f}s" fill="freeze"/>')
              + '</text>')
            cx = X0 + len(prompt) * CW
            a(f'<rect x="{cx:.1f}" y="{y - FS + 2}" width="{CW:.1f}" height="{FS + 3}" fill="{t["ink"]}" '
              f'opacity="{1 if STATIC else 0}">'
              + ("" if STATIC else
                 # pisca por uns 15 s e fica aceso: repeticao infinita deixa o Chrome
                 # headless sem quadro estavel (tela em branco no print)
                 f'<animate attributeName="opacity" values="1;0;1" keyTimes="0;0.5;1" calcMode="discrete" '
                 f'dur="1.1s" begin="{relogio:.2f}s" repeatCount="14" fill="freeze"/>')
              + '</rect>')

    a('</svg>')
    salvar(f"terminal-{tema}.svg", p)


# ── diagramas ───────────────────────────────────────────────────────────────

class Prancha:
    """Caixas, chips e setas num SVG monocromatico."""

    def __init__(self, tema, W, H, rotulo):
        self.t = TEMAS[tema]
        self.W, self.H = W, H
        self.p = []
        t = self.t
        self.p.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
                      f'height="{H}" role="img" aria-label="{esc(rotulo)}">')
        self.p.append('<defs><marker id="ponta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                      f'markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9" fill="none" '
                      f'stroke="{t["dim"]}" stroke-width="1.6"/></marker>'
                      f'<pattern id="malha" width="24" height="24" patternUnits="userSpaceOnUse">'
                      f'<circle cx="1" cy="1" r="0.9" fill="{t["line"]}" fill-opacity="0.09"/></pattern></defs>')
        self.p.append(f'<rect width="{W}" height="{H}" rx="10" fill="{t["bg"]}"/>')
        self.p.append(f'<rect width="{W}" height="{H}" rx="10" fill="url(#malha)"/>')
        self.p.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="none" '
                      f'stroke="{t["line"]}" stroke-opacity="0.14"/>')

    def secao(self, x, y, texto):
        t = self.t
        self.p.append(f'<line x1="{x}" y1="{y - 4}" x2="{x + 22}" y2="{y - 4}" stroke="{t["ink"]}" stroke-width="2"/>')
        self.p.append(f'<text x="{x + 32}" y="{y}" font-family="{MONO}" font-size="11" letter-spacing="2.2" '
                      f'fill="{t["dim"]}">{esc(texto.upper())}</text>')

    def caixa(self, x, y, w, h, titulo, subs=(), forte=False):
        t = self.t
        self.p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{t["panel"]}" '
                      f'stroke="{t["line"]}" stroke-opacity="{0.55 if forte else 0.2}"/>')
        self.p.append(f'<text x="{x + 14}" y="{y + 24}" font-family="{MONO}" font-size="13.5" '
                      f'font-weight="700" fill="{t["ink"]}">{esc(titulo)}</text>')
        for i, s in enumerate(subs):
            self.p.append(f'<text x="{x + 14}" y="{y + 43 + i * 16}" font-family="{MONO}" font-size="11.5" '
                          f'fill="{t["dim"]}">{esc(s)}</text>')

    def chips(self, x, y, itens, maxw):
        """Chips em linha, quebrando quando passa de maxw. Devolve o y da ultima linha."""
        t = self.t
        cx, cy = x, y
        for item in itens:
            w = len(item) * 11.5 * 0.602 + 18
            if cx + w > x + maxw:
                cx, cy = x, cy + 30
            self.p.append(f'<rect x="{cx:.1f}" y="{cy}" width="{w:.1f}" height="22" rx="4" fill="{t["chip"]}" '
                          f'stroke="{t["line"]}" stroke-opacity="0.12"/>')
            self.p.append(f'<text x="{cx + 9:.1f}" y="{cy + 15}" font-family="{MONO}" font-size="11.5" '
                          f'fill="{t["ink"]}" fill-opacity="0.85">{esc(item)}</text>')
            cx += w + 8
        return cy

    def seta(self, pontos, rotulo=None, rx=None, ry=None, tracejada=False):
        t = self.t
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pontos)
        dash = ' stroke-dasharray="4 4"' if tracejada else ""
        self.p.append(f'<path d="{d}" fill="none" stroke="{t["dim"]}" stroke-width="1.2"{dash} '
                      f'marker-end="url(#ponta)"/>')
        if rotulo:
            self.p.append(f'<text x="{rx}" y="{ry}" text-anchor="middle" font-family="{MONO}" font-size="10.5" '
                          f'fill="{t["dim"]}">{esc(rotulo)}</text>')

    def fechar(self, nome):
        self.p.append('</svg>')
        salvar(nome, self.p)


def diagrama_lyx(tema):
    W, H = 1200, 590
    d = Prancha(tema, W, H, "Diagram of the Lyx platform I work on: external sources feed a NestJS modular "
                            "monolith and a Python ETL; both land in Postgres and are read by Next.js fronts "
                            "and BI; every change goes through a delivery loop of pull request, CI audit gate, "
                            "AI review agent, deploy train and production.")
    d.secao(32, 40, "Lyx Engenharia · what I build and run")

    # fontes
    d.secao(32, 76, "sources")
    fontes = [("SAP ERP", "orders · suppliers"),
              ("Construction API", "sites · contracts · QA"),
              ("Permit portals", "municipal, scraped"),
              ("MS Project .mpp", "site schedules"),
              ("Spreadsheets", "planning · finance")]
    fy = []
    for i, (n, s) in enumerate(fontes):
        y = 92 + i * 64
        d.caixa(32, y, 196, 50, n, [s])
        fy.append(y + 25)

    # hub
    hx, hy, hw, hh = 300, 92, 470, 178
    d.caixa(hx, hy, hw, hh, "Hub · NestJS modular monolith on Bun", forte=True)
    d.chips(hx + 14, hy + 40, ["controladoria/", "medições/", "legalização/"], hw - 28)
    d.chips(hx + 14, hy + 72, ["shared/integracoes/  ← only door out"], hw - 28)
    d.chips(hx + 14, hy + 104, ["approval flows", "retention & bonds", "rework", "scrapers"], hw - 28)
    d.chips(hx + 14, hy + 136, ["structured events → Axiom"], hw - 28)

    # etl
    ex, ey, ew, eh = 300, 300, 470, 120
    d.caixa(ex, ey, ew, eh, "Data · Python ETL on Airflow", forte=True)
    d.chips(ex + 14, ey + 40, ["MPXJ: reads .mpp natively", "idempotent loads"], ew - 28)
    d.chips(ex + 14, ey + 72, ["quality", "PPC", "S-curve", "finance"], ew - 28)

    # bus das fontes
    bh, be = 262, 280
    ligacoes = [(0, "h"), (1, "h"), (1, "e"), (2, "h"), (3, "e"), (4, "e")]
    for i, alvo in ligacoes:
        y = fy[i]
        if alvo == "h":
            ty = min(max(y, hy + 20), hy + hh - 20)
            d.seta([(228, y), (bh, y), (bh, ty), (hx - 2, ty)])
        else:
            ty = min(max(y, ey + 20), ey + eh - 20)
            d.seta([(228, y), (be, y), (be, ty), (ex - 2, ty)])

    # direita
    d.caixa(820, 92, 160, 64, "Postgres", ["Drizzle migrations"])
    d.caixa(820, 206, 160, 64, "Next.js fronts", ["3 apps"])
    d.seta([(hx + hw, 124), (818, 124)])
    d.seta([(818, 238), (hx + hw + 2, 238)])
    d.caixa(820, 300, 160, 64, "BI warehouse", ["Postgres"])
    d.caixa(1012, 300, 156, 64, "BI · Next.js", ["dashboards"])
    d.seta([(ex + ew, 332), (818, 332)])
    d.seta([(980, 332), (1010, 332)])
    d.caixa(1012, 92, 156, 178, "Axiom", ["structured logs", "per-event fields", "", "LGPD: aggregates", "only, no PII out"])
    d.seta([(740, hy), (740, 80), (1090, 80), (1090, 90)], tracejada=True)

    # loop de entrega
    d.secao(32, 470, "delivery loop · every change, no exceptions")
    etapas = [("Claude Code", ["hooks · autoreview", "team memory (MCP)"]),
              ("Pull request", ["small, one subject", "linked to a task"]),
              ("CI audit gate", ["types · tests", "LGPD / PII gate"]),
              ("AI review agent", ["approves or", "requests changes"]),
              ("Deploy train", ["scheduled windows", "migrations ride it"]),
              ("Production", ["daily deploy check", "commit on /health"])]
    n = len(etapas)
    gap = 26
    w = (W - 64 - gap * (n - 1)) / n
    for i, (tt, ss) in enumerate(etapas):
        x = 32 + i * (w + gap)
        d.caixa(round(x), 488, round(w), 72, tt, ss, forte=(i in (0, n - 1)))
        if i < n - 1:
            d.seta([(x + w + 2, 524), (x + w + gap - 2, 524)])
    d.fechar(f"lyx-{tema}.svg")


def diagrama_trackside(tema):
    W, H = 1200, 400
    d = Prancha(tema, W, H, "Trackside architecture: a Tauri 2 window talks over a Unix socket to a Rust core "
                            "process that owns the PTY sessions; agents run in those PTYs and their tool calls "
                            "pass through an MCP gateway and an agent hook that apply your policy file and "
                            "write to a hash-chained audit trail before the call happens.")
    d.secao(32, 40, "Trackside · architecture")

    d.caixa(32, 70, 280, 170, "Window · Tauri 2 + SolidJS", forte=True)
    d.chips(46, 110, ["xterm panes", "split & drag", "policy editor", "multi-agent tree", "7 languages"], 252)

    d.caixa(400, 70, 380, 170, "Core · Rust, own process", forte=True)
    d.chips(414, 110, ["PTY sessions", "outlive the window", "resume after crash",
                       "token & cost meter", "workflow engine"], 352)
    d.seta([(312, 140), (398, 140)])
    d.seta([(398, 172), (314, 172)])
    d.p.append(f'<text x="356" y="124" text-anchor="middle" font-family="{MONO}" font-size="10.5" '
               f'fill="{d.t["dim"]}">unix</text>')
    d.p.append(f'<text x="356" y="196" text-anchor="middle" font-family="{MONO}" font-size="10.5" '
               f'fill="{d.t["dim"]}">socket</text>')

    d.caixa(868, 70, 300, 64, "Agents in PTYs", ["Claude Code · Codex · Ollama"])
    d.seta([(780, 102), (866, 102)])

    d.caixa(868, 176, 142, 64, "MCP gateway", ["allow·ask·deny"])
    d.caixa(1026, 176, 142, 64, "Agent hook", ["by tool & path"])
    d.seta([(939, 134), (939, 174)], "tool call", 980, 158)
    d.seta([(1097, 134), (1097, 174)])

    y2 = 300
    d.caixa(32, y2, 280, 64, "WASM plugins", ["wasmi · no host access", "instruction & memory ceilings"])
    d.caixa(400, y2, 380, 64, "Policy file", ["yours, plain text, checked before save"])
    d.caixa(868, y2, 300, 64, "Audit trail", ["hash-chained · written before", "the call runs · verify & export"],
            forte=True)
    d.seta([(172, 240), (172, 298)], tracejada=True)
    d.seta([(939, 240), (939, 298)])
    d.seta([(1097, 240), (1097, 298)])
    d.seta([(590, 298), (590, 262), (900, 262), (900, 242)], tracejada=True)
    d.p.append(f'<text x="745" y="256" text-anchor="middle" font-family="{MONO}" font-size="10.5" '
               f'fill="{d.t["dim"]}">rules</text>')
    d.fechar(f"trackside-{tema}.svg")


if __name__ == "__main__":
    for tema in TEMAS:
        terminal(tema)
        diagrama_lyx(tema)
        diagrama_trackside(tema)
