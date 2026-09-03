# -*- coding: utf-8 -*-
"""Gera o cartao de atividade do perfil.

Nao uso github-readme-stats: o servico estava devolvendo 503 e imagem quebrada
num perfil e pior do que nao ter cartao nenhum. Aqui os numeros saem da API do
GitHub e viram um SVG commitado no repo, no mesmo desenho do banner.

Conta so repositorio **publico e nao-fork** — o que qualquer visitante consegue
conferir, e o mesmo resultado rodando aqui ou no GitHub Actions.

    GH_TOKEN=$(gh auth token) python3 scripts/gen_stats.py
"""
import json
import os
import subprocess
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = f"{RAIZ}/assets/stats.svg"
USUARIO = "EnzoKoeche"

W, H = 1200, 250
FUNDO = "#0a0f0e"
ACENTO = "#00e5c0"
CLARO = "#e6f1ef"
APAGADO = "#7d918d"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

CONSULTA = """
query($login: String!) {
  user(login: $login) {
    createdAt
    followers { totalCount }
    contributionsCollection {
      contributionCalendar { totalContributions }
      totalCommitContributions
    }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      totalCount
      nodes {
        languages(first: 12, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""


def token():
    t = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if t:
        return t
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()


def buscar():
    corpo = json.dumps({"query": CONSULTA, "variables": {"login": USUARIO}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql", data=corpo,
        headers={"Authorization": f"bearer {token()}",
                 "Content-Type": "application/json",
                 "User-Agent": "perfil-enzokoeche"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    if "errors" in d:
        raise SystemExit(f"GraphQL reclamou: {d['errors']}")
    return d["data"]["user"]


def compacto(n):
    if n >= 1000:
        seco = f"{n / 1000:.1f}".rstrip("0").rstrip(".")
        return seco + "k"
    return str(n)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    u = buscar()
    repos = u["repositories"]["nodes"]
    cc = u["contributionsCollection"]

    bytes_por_lang = {}
    for r in repos:
        for e in r["languages"]["edges"]:
            bytes_por_lang[e["node"]["name"]] = bytes_por_lang.get(e["node"]["name"], 0) + e["size"]
    total = sum(bytes_por_lang.values()) or 1
    # menos de 1% vira "Other": fatia invisivel com rotulo grande so suja a legenda
    ordenado = sorted(bytes_por_lang.items(), key=lambda kv: -kv[1])
    top = [(n, v) for n, v in ordenado if v / total >= 0.01][:6]
    resto = total - sum(v for _, v in top)
    fatias = top + ([("Other", resto)] if resto > 0 else [])

    # do acento pro apagado, pra barra ler como uma escala e nao como confete
    tons = ["#00e5c0", "#12b79c", "#1c8e7c", "#22685e", "#274b46", "#2b3733", "#222b2a"]

    # estrelas e seguidores ficam de fora de proposito: numero baixo em cartao
    # de perfil nao informa nada e so chama atencao pro que nao interessa.
    desde = u["createdAt"][:4]
    numeros = [
        (compacto(u["repositories"]["totalCount"]), "public repos"),
        (compacto(cc["totalCommitContributions"]), "commits · 12 mo"),
        (compacto(cc["contributionCalendar"]["totalContributions"]), "contributions · 12 mo"),
        (str(len(bytes_por_lang)), "languages shipped"),
        (desde, "on github since"),
    ]

    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="Activity for {USUARIO}">')
    a(f'<rect width="{W}" height="{H}" rx="6" fill="{FUNDO}"/>')
    a(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="6" fill="none" '
      f'stroke="{CLARO}" stroke-opacity="0.08"/>')

    x0 = 56
    a(f'<line x1="{x0}" y1="46" x2="{x0+40}" y2="46" stroke="{ACENTO}" stroke-width="2"/>')
    a(f'<text x="{x0+56}" y="50" font-family="{MONO}" font-size="12" letter-spacing="2.6" '
      f'fill="{APAGADO}">ACTIVITY</text>')

    # ── numeros ──────────────────────────────────────────────────────────
    passo = (W - x0 * 2) / len(numeros)
    for i, (valor, rotulo) in enumerate(numeros):
        x = x0 + passo * i
        a(f'<text x="{x:.0f}" y="118" font-family="{SANS}" font-size="42" font-weight="300" '
          f'fill="{CLARO}">{valor}</text>')
        a(f'<text x="{x:.0f}" y="142" font-family="{MONO}" font-size="11" letter-spacing="1.4" '
          f'fill="{APAGADO}">{esc(rotulo).upper()}</text>')

    # ── barra de linguagens ──────────────────────────────────────────────
    by, bh, bw = 186, 8, W - x0 * 2
    a(f'<text x="{x0}" y="174" font-family="{MONO}" font-size="11" letter-spacing="2.2" '
      f'fill="{APAGADO}" fill-opacity="0.75">LANGUAGES · PUBLIC REPOS</text>')
    cur = x0
    for i, (nome, tam) in enumerate(fatias):
        largura = bw * tam / total
        r = 'rx="4"' if i in (0, len(fatias) - 1) else ""
        a(f'<rect x="{cur:.1f}" y="{by}" width="{max(largura - 2, 1):.1f}" height="{bh}" {r} '
          f'fill="{tons[min(i, len(tons)-1)]}"/>')
        cur += largura

    lx = x0
    for i, (nome, tam) in enumerate(fatias):
        pct = 100 * tam / total
        a(f'<circle cx="{lx+4:.0f}" cy="{by+40}" r="3.5" fill="{tons[min(i, len(tons)-1)]}"/>')
        a(f'<text x="{lx+16:.0f}" y="{by+44}" font-family="{SANS}" font-size="13" fill="{APAGADO}">'
          f'{esc(nome)} <tspan fill="{CLARO}" fill-opacity="0.55">{pct:.1f}%</tspan></text>')
        lx += 26 + len(nome) * 7.4 + 40

    a('</svg>')
    open(SAIDA, "w", encoding="utf-8").write("\n".join(p) + "\n")
    print(f"{SAIDA}  repos={u['repositories']['totalCount']} "
          f"commits={cc['totalCommitContributions']} "
          f"contrib={cc['contributionCalendar']['totalContributions']} "
          f"langs={[n for n, _ in fatias]}")


if __name__ == "__main__":
    main()
