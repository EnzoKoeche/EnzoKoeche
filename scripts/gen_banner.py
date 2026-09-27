# -*- coding: utf-8 -*-
"""Gera o banner do perfil.

Mesma ideia das placas do portfolio: nada de imagem baixada, a geometria e
desenhada aqui a partir de uma semente fixa, entao todo run devolve o mesmo
SVG. Fundo escuro, um acento so, filete fino.

    python3 scripts/gen_banner.py
"""
import math
import os
import random

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = f"{RAIZ}/assets/banner.svg"

W, H = 1200, 340
FUNDO = "#0a0f0e"
ACENTO = "#00e5c0"
CLARO = "#e6f1ef"
APAGADO = "#7d918d"
PRANCHA = "#7da2ff"  # azul de blueprint, o traco estrutural do site
SEMENTE = 190126  # 19/01/26 — nada de especial, so pra travar o desenho

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def campo(rng, n=34):
    """Nos espalhados na metade direita, com distancia minima entre eles.

    Amostragem por rejeicao: e o suficiente pra esse tamanho e evita a mancha
    de pontos grudados que sai do random puro.
    """
    pts, tentativas = [], 0
    while len(pts) < n and tentativas < 6000:
        tentativas += 1
        x = rng.uniform(W * 0.46, W - 76)
        y = rng.uniform(46, H - 46)
        # afina perto da esquerda, pra nao competir com o nome
        if rng.random() > (x - W * 0.42) / (W * 0.55):
            continue
        if all((x - px) ** 2 + (y - py) ** 2 > 66 ** 2 for px, py in pts):
            pts.append((x, y))
    return pts


def arestas(pts, k=2):
    """Liga cada no aos k vizinhos mais proximos, sem repetir par."""
    vistos, saida = set(), []
    for i, a in enumerate(pts):
        d = sorted(range(len(pts)), key=lambda j: (pts[j][0] - a[0]) ** 2 + (pts[j][1] - a[1]) ** 2)
        for j in d[1:k + 1]:
            par = (min(i, j), max(i, j))
            if par not in vistos:
                vistos.add(par)
                saida.append((a, pts[j]))
    return saida


def main():
    rng = random.Random(SEMENTE)
    pts = campo(rng)
    linhas = arestas(pts)

    p = []
    a = p.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="Enzo Koeche — Software Engineer, Applied AI">')
    a('<defs>')
    a(f'<linearGradient id="ceu" x1="0" y1="0" x2="1" y2="1">'
      f'<stop offset="0" stop-color="#0c1211"/><stop offset="1" stop-color="{FUNDO}"/></linearGradient>')
    a(f'<radialGradient id="brilho" cx="0.74" cy="0.44" r="0.52">'
      f'<stop offset="0" stop-color="{ACENTO}" stop-opacity="0.13"/>'
      f'<stop offset="1" stop-color="{ACENTO}" stop-opacity="0"/></radialGradient>')
    # apaga o grafo conforme ele se aproxima do texto
    a('<linearGradient id="sumico" x1="0" y1="0" x2="1" y2="0">'
      '<stop offset="0" stop-color="#000"/><stop offset="0.34" stop-color="#000"/>'
      '<stop offset="0.62" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient>')
    a('<mask id="daDireita"><rect width="100%" height="100%" fill="url(#sumico)"/></mask>')
    a('</defs>')

    a(f'<rect width="{W}" height="{H}" fill="url(#ceu)"/>')
    a(f'<rect width="{W}" height="{H}" fill="url(#brilho)"/>')

    # ── prancha: malha, moldura e miras de canto (a identidade do site) ────
    a(f'<g stroke="{PRANCHA}">')
    for gx in range(0, W + 1, 24):
        forte = gx % 120 == 0
        a(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke-opacity="{0.05 if forte else 0.02}" stroke-width="1"/>')
    for gy in range(0, H + 1, 24):
        forte = gy % 120 == 0
        a(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke-opacity="{0.05 if forte else 0.02}" stroke-width="1"/>')
    a('</g>')
    a(f'<rect x="10" y="10" width="{W - 20}" height="{H - 20}" fill="none" '
      f'stroke="{PRANCHA}" stroke-opacity="0.22" stroke-width="1"/>')
    for cx, cy in [(10, 10), (W - 10, 10), (10, H - 10), (W - 10, H - 10)]:
        a(f'<g stroke="{PRANCHA}" stroke-opacity="0.55" stroke-width="1">'
          f'<line x1="{cx - 8}" y1="{cy}" x2="{cx + 8}" y2="{cy}"/>'
          f'<line x1="{cx}" y1="{cy - 8}" x2="{cx}" y2="{cy + 8}"/></g>'
          f'<circle cx="{cx}" cy="{cy}" r="4" fill="none" stroke="{PRANCHA}" stroke-opacity="0.35"/>')

    # ── grafo ────────────────────────────────────────────────────────────
    a('<g mask="url(#daDireita)">')
    for (x1, y1), (x2, y2) in linhas:
        o = 0.30 - 0.16 * (math.hypot(x2 - x1, y2 - y1) / 190)
        a(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
          f'stroke="{ACENTO}" stroke-opacity="{max(o, 0.05):.2f}" stroke-width="0.9"/>')
    for i, (x, y) in enumerate(pts):
        forte = i % 7 == 0
        a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{2.6 if forte else 1.7:.1f}" fill="{ACENTO}" '
          f'fill-opacity="{0.85 if forte else 0.34:.2f}"/>')
        if forte:
            a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="none" stroke="{ACENTO}" '
              f'stroke-opacity="0.22" stroke-width="0.8"/>')
    a('</g>')

    # ── texto ────────────────────────────────────────────────────────────
    x0 = 72
    a(f'<line x1="{x0}" y1="96" x2="{x0 + 56}" y2="96" stroke="{ACENTO}" stroke-width="2"/>')
    a(f'<text x="{x0}" y="176" font-family="{SANS}" font-size="66" font-weight="300" '
      f'letter-spacing="7" fill="{CLARO}">ENZO KOECHE</text>')
    a(f'<text x="{x0}" y="212" font-family="{SANS}" font-size="19" font-weight="400" '
      f'letter-spacing="1.2" fill="{APAGADO}">Software Engineer '
      f'<tspan fill="{ACENTO}">·</tspan> Applied AI</text>')
    a(f'<text x="{x0}" y="278" font-family="{MONO}" font-size="12.5" letter-spacing="2.6" '
      f'fill="{APAGADO}" fill-opacity="0.8">CURITIBA, BRAZIL · 25°26′S 49°16′W</text>')
    # cota: linha com tiques perpendiculares, como no desenho tecnico
    cx1, cx2, cy = x0 + 372, int(W * 0.47), 274
    a(f'<g stroke="{PRANCHA}" stroke-opacity="0.45" stroke-width="1">'
      f'<line x1="{cx1}" y1="{cy}" x2="{cx2}" y2="{cy}"/>'
      f'<line x1="{cx1}" y1="{cy - 5}" x2="{cx1}" y2="{cy + 5}"/>'
      f'<line x1="{cx2}" y1="{cy - 5}" x2="{cx2}" y2="{cy + 5}"/></g>')

    # ── mini-carimbo: o quadro de titulo da prancha, canto inferior direito ─
    cw, ch = 236, 54
    cx, cy = W - 10 - cw, H - 10 - ch
    a(f'<g font-family="{MONO}">')
    a(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" fill="{FUNDO}" fill-opacity="0.72" '
      f'stroke="{PRANCHA}" stroke-opacity="0.4" stroke-width="1"/>')
    a(f'<line x1="{cx}" y1="{cy + 27}" x2="{cx + cw}" y2="{cy + 27}" stroke="{PRANCHA}" stroke-opacity="0.25"/>')
    a(f'<line x1="{cx + 118}" y1="{cy + 27}" x2="{cx + 118}" y2="{cy + ch}" stroke="{PRANCHA}" stroke-opacity="0.25"/>')
    a(f'<text x="{cx + 10}" y="{cy + 18}" font-size="9.5" letter-spacing="2.2" fill="{APAGADO}">PROJETO: ENZO KOECHE</text>')
    a(f'<text x="{cx + 10}" y="{cy + 45}" font-size="9.5" letter-spacing="2.2" fill="{APAGADO}">ESC 1:1</text>')
    a(f'<text x="{cx + 128}" y="{cy + 45}" font-size="9.5" letter-spacing="2.2" fill="{ACENTO}">FL. 01/01</text>')
    a('</g>')
    a('</svg>')

    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    open(SAIDA, "w", encoding="utf-8").write("\n".join(p) + "\n")
    print(f"{SAIDA}  ({os.path.getsize(SAIDA) / 1024:.1f} KB, {len(pts)} nos, {len(linhas)} arestas)")


if __name__ == "__main__":
    main()
