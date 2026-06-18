#!/usr/bin/env python3
from pathlib import Path
from html import escape

BASE = Path(__file__).resolve().parent
EVENT_URL = "https://event.as-for-me.com/dunhwa-flower-cards"
LOGO = "../assets/asify-logo-horizontal-purple.png"

CARDS = [
    {
        "slug": "morning-glory",
        "flower": "牽牛花",
        "theme": "重新打開",
        "title": "一朵會在早晨打開的花",
        "lead": "也許今天，妳也正在重新打開一個新的自己。",
        "meaning": "妳不需要一次變成很厲害的人。今天願意走進來，就是一個新的開始。",
        "story_title": "從一個小配件，重新回到自己的節奏",
        "story": [
            "牽牛花在早晨打開，像是身體剛開始重新回到自己的節奏。",
            "第一次來 ASify，不一定要馬上知道自己適合哪一件。妳可以先摸摸布料、試試版型，也可以從一個小配件開始。髮帶不是主角，卻會讓練習和日常都少一點干擾。"
        ],
        "note": "今天可以慢慢逛：先從觸感開始，再讓身體告訴妳答案。",
        "chips": ["髮帶與配件", "止滑襪", "無痕內褲", "十分褲", "九分褲"],
        "gift": "開卡<br>送髮帶",
        "gift_copy": "抽到牽牛花，今天在敦化店開卡，送妳一條髮帶。讓今天的練習、試穿和日常，都少一點被打擾。",
        "rules": ["限 ASify 敦化店當日使用。", "每次來店都可以抽一張花卡，不需消費。", "限定正價商品，不可與其他優惠併用。", "贈品數量有限，送完為止。", "店員以現場抽到的實體花卡與手機頁面確認。"],
        "palette": ("#6975ac", "#4f5085", "#c9dfdd", "#526b4e", "#324531", "#c99a4c"),
        "svg": "morning-glory",
    },
    {
        "slug": "jasmine",
        "flower": "茉莉",
        "theme": "清爽靠近",
        "title": "安靜靠近，也很有存在感",
        "lead": "妳抽到的是一朵看起來安靜、靠近時卻很有存在感的花。",
        "meaning": "妳可以很溫柔，也可以很清楚。清爽不是疏離，是讓自己有空間呼吸。",
        "story_title": "把夏天穿得清爽一點",
        "story": [
            "茉莉的感覺很乾淨，適合連到 ASify 夏天最需要的「不黏、不悶、流汗後也不要有負擔」。",
            "如果妳怕熱、怕厚重，極薄布會是第一個可以試的方向；如果妳想要上半身也清爽，500 回眸美背上衣或好自由側綁背心也很適合一起看。"
        ],
        "note": "今天適合試試清爽、輕薄、讓身體有空間呼吸的搭配。",
        "chips": ["極薄布褲款", "500 回眸美背上衣", "好自由側綁背心", "止滑襪"],
        "gift": "消費即送<br>止滑襪",
        "gift_copy": "抽到茉莉，今天在敦化店消費即送止滑襪。給皮拉提斯、伸展與日常練習，多一點踏實的安心感。",
        "rules": ["限 ASify 敦化店當日使用。", "每次來店都可以抽一張花卡，不需消費。", "限定正價商品，不可與其他優惠併用。", "贈品數量有限，送完為止。", "店員以現場抽到的實體花卡與手機頁面確認。"],
        "palette": ("#f7f2dc", "#a58b42", "#dfeee8", "#5f7a63", "#344d3d", "#c7a45b"),
        "svg": "jasmine",
    },
    {
        "slug": "water-lily",
        "flower": "睡蓮",
        "theme": "把身體放回水面",
        "title": "不是不努力，是懂得被承接",
        "lead": "妳抽到的是一朵浮在水面上的花。",
        "meaning": "有些日子，妳不需要再更用力。讓身體安靜下來，也是一種前進。",
        "story_title": "柔軟不是鬆掉，是身體被好好接住",
        "story": [
            "睡蓮適合連到慕斯布和軟棉棉罩衫。慕斯布是 ASify 最柔軟、最像第二層肌膚的布料，適合瑜珈、皮拉提斯、芭蕾舞、冥想等低強度運動。",
            "軟棉棉罩衫則像薄薄的一層空氣，冷氣房、通勤、練習前後都能披上。"
        ],
        "note": "今天可以試試柔軟一點的布料，讓身體慢慢回到自己的位置。",
        "chips": ["慕斯布十分褲", "慕斯布九分褲", "軟棉棉罩衫", "Dare to Dream 瑜伽寬褲"],
        "gift": "滿 3999<br>再送運動毛巾",
        "gift_copy": "抽到睡蓮，今天在敦化店消費滿 3999，再送運動毛巾。原門市滿額贈規則照常依現場公告，這張是花卡加碼。",
        "rules": ["限 ASify 敦化店當日使用。", "每次來店都可以抽一張花卡，不需消費。", "限定正價商品，不可與其他優惠併用。", "此贈品為花卡加碼；原門市滿額贈規則照常依現場公告。", "贈品數量有限，送完為止。", "店員以現場抽到的實體花卡與手機頁面確認。"],
        "palette": ("#dba3bc", "#9b5e83", "#dbe9ed", "#5f7c7e", "#334f55", "#b9915a"),
        "svg": "water-lily",
    },
    {
        "slug": "sunflower",
        "flower": "向日葵",
        "theme": "站到光裡",
        "title": "妳可以被看見",
        "lead": "妳抽到的是一朵會轉向光的花。",
        "meaning": "妳可以被看見，不需要先把自己縮小。",
        "story_title": "好的版型，陪妳重新看見自己",
        "story": [
            "向日葵適合連到 ASify 的招牌褲款：十分褲和九分褲。",
            "十分褲是踩腳設計，視覺上拉長比例；九分褲到腳踝，是很多人最容易日常穿、練習穿的經典款。這張卡想提醒妳：不是身材準備好了才可以穿好看的褲子，而是好的版型會陪妳重新看見自己。"
        ],
        "note": "今天適合把經典款試起來，看看哪一種比例最像妳。",
        "chips": ["十分褲", "九分褲", "果凍布", "極薄布"],
        "gift": "整單<br>85 折",
        "gift_copy": "抽到向日葵，今天在敦化店正價商品整單 85 折。讓妳把想試很久的那件，帶進真正的日常。",
        "rules": ["限 ASify 敦化店當日使用。", "每次來店都可以抽一張花卡，不需消費。", "限定正價商品，不可與其他優惠併用。", "店員以現場抽到的實體花卡與手機頁面確認。"],
        "palette": ("#f5bd3f", "#b16d22", "#f6e9bd", "#627243", "#3f512f", "#d29b2c"),
        "svg": "sunflower",
    },
    {
        "slug": "hibiscus",
        "flower": "扶桑花",
        "theme": "剛剛好的亮",
        "title": "亮得剛好，不用用力",
        "lead": "妳抽到的是一朵很夏天的花。",
        "meaning": "妳不用很用力地吸引目光。真正適合妳的亮，是舒服地長在妳身上。",
        "story_title": "把一點夏天，收進身上",
        "story": [
            "扶桑花有夏天的明亮感，適合連到 Hebe 青春女神 U 型美背 Bratop 橘色。",
            "Hebe 是日常外穿、輕度運動都可以穿的 Bratop，U 型美背露出剛剛好的優雅；橘色則像把一點夏天收進身上，不誇張，但會讓人覺得氣色很好。"
        ],
        "note": "今天適合試試一件能外穿、也能輕鬆活動的 Bratop。",
        "chips": ["Hebe 青春女神 U 型美背 Bratop", "日常外穿 Bratop", "九分褲", "寬褲"],
        "gift": "買一件正價商品<br>送 Hebe 橘色",
        "gift_copy": "抽到扶桑花，今天在敦化店消費一個正價商品，即送 Hebe 青春女神 U 型美背 Bratop 橘色。",
        "rules": ["限 ASify 敦化店當日使用。", "每次來店都可以抽一張花卡，不需消費。", "消費一個正價商品即贈 Hebe Bratop 橘色。", "不可與其他優惠併用。", "尺寸與數量依現場庫存為準，送完為止。", "店員以現場抽到的實體花卡與手機頁面確認。"],
        "palette": ("#ee7451", "#ad3f47", "#f6d2bf", "#66764c", "#425432", "#d49443"),
        "svg": "hibiscus",
    },
    {
        "slug": "frangipani",
        "flower": "雞蛋花",
        "theme": "躺進夏天",
        "title": "舒服不是偷懶",
        "lead": "妳抽到的是一朵像假期一樣的花。",
        "meaning": "生活已經夠忙了。妳可以選一種不用繃緊，也很好看的方式。",
        "story_title": "留一點空氣，給身體自在切換",
        "story": [
            "雞蛋花適合連到 ASify 的寬鬆線：闊腿褲、Dare to Dream 瑜伽寬褲、軟棉棉罩衫。",
            "這些單品不是為了把身體藏起來，而是讓腿和布料之間留一點空氣，讓妳從工作、通勤、練習到週末都能自在切換。"
        ],
        "note": "今天可以試試不緊繃、但依然有型的舒適線條。",
        "chips": ["闊腿褲", "Dare to Dream 瑜伽寬褲", "軟棉棉罩衫", "ASify 字母背心"],
        "gift": "任選商品<br>買二送一",
        "gift_copy": "抽到雞蛋花，今天在敦化店任選商品買二送一，依價高者計算。適合一次把日常、練習、週末都配好。",
        "rules": ["限 ASify 敦化店當日使用。", "每次來店都可以抽一張花卡，不需消費。", "限定正價商品，不可與其他優惠併用。", "任選商品買二送一，依價高者計算。", "店員以現場抽到的實體花卡與手機頁面確認。"],
        "palette": ("#f7f1d2", "#d7a43f", "#d7ece2", "#667a56", "#3d5338", "#c89d4a"),
        "svg": "frangipani",
    },
]


def flower_svg(kind: str) -> str:
    if kind == "jasmine":
        petals = "".join(
            f'<ellipse cx="{320 + dx}" cy="{230 + dy}" rx="58" ry="96" transform="rotate({rot} {320 + dx} {230 + dy})" fill="url(#petalGrad)"/>'
            for dx, dy, rot in [(0, -72, 0), (66, -20, 58), (44, 58, 132), (-44, 58, 228), (-66, -20, 302)]
        )
        return f'{vine()}<g class="flower-main">{petals}<circle cx="320" cy="230" r="34" fill="#f1c76e"/><circle cx="320" cy="230" r="14" fill="#a58b42"/></g>{sparkles()}'
    if kind == "water-lily":
        petals = "".join(
            f'<ellipse cx="320" cy="255" rx="52" ry="142" transform="rotate({rot} 320 255)" fill="url(#petalGrad)" opacity="{op}"/>'
            for rot, op in [(0, .9), (38, .82), (76, .78), (114, .82), (152, .9), (190, .82), (228, .78), (266, .82), (304, .9)]
        )
        return f'<ellipse cx="320" cy="555" rx="210" ry="78" fill="#7aa0a3" opacity=".32"/>{vine()}{petals}<circle cx="320" cy="255" r="36" fill="#f6d56f"/>{sparkles()}'
    if kind == "sunflower":
        petals = "".join(
            f'<ellipse cx="320" cy="245" rx="42" ry="120" transform="rotate({rot} 320 245)" fill="url(#petalGrad)"/>'
            for rot in range(0, 360, 24)
        )
        return f'{vine()}{petals}<circle cx="320" cy="245" r="82" fill="#61442d"/><circle cx="320" cy="245" r="54" fill="#3b2d27" opacity=".9"/>{sparkles()}'
    if kind == "hibiscus":
        petals = "".join(
            f'<path d="M320 252 C{240+x} {104+y} {390+x} {60+y} {400+x} {204+y} C392 314 330 342 320 252Z" transform="rotate({rot} 320 252)" fill="url(#petalGrad)" opacity=".92"/>'
            for x, y, rot in [(0, 0, 0), (8, 10, 72), (-12, 4, 144), (8, -6, 216), (-4, 10, 288)]
        )
        return f'{vine()}{petals}<path d="M320 252 C350 292 366 338 384 398" stroke="#f1cc79" stroke-width="10" stroke-linecap="round" fill="none"/><circle cx="389" cy="410" r="15" fill="#e5ba55"/>{sparkles()}'
    if kind == "frangipani":
        petals = "".join(
            f'<path d="M320 252 C260 128 348 84 386 164 C422 241 350 290 320 252Z" transform="rotate({rot} 320 252)" fill="url(#petalGrad)" opacity=".96"/>'
            for rot in range(0, 360, 72)
        )
        return f'{vine()}{petals}<circle cx="320" cy="252" r="42" fill="#edc656"/><circle cx="320" cy="252" r="18" fill="#d7a43f"/>{sparkles()}'
    return f'{vine()}<g class="flower-main"><ellipse cx="329" cy="189" rx="165" ry="151" fill="#d9e7df" opacity=".58"/><path d="M320 92 C406 40 514 92 527 196 C542 314 433 394 323 348 C217 397 100 321 112 199 C123 88 229 37 320 92Z" fill="url(#petalGrad)"/><circle cx="322" cy="333" r="36" fill="#fff6c9"/><circle cx="322" cy="333" r="17" fill="#c99a4c"/></g>{sparkles()}'


def vine() -> str:
    return """<path class="vine" d="M330 740 C294 650 381 592 336 515 C291 438 181 482 156 398 C129 305 246 257 230 174" fill="none" stroke="var(--leaf)" stroke-width="10" stroke-linecap="round"/>
<path class="vine" d="M313 625 C251 603 220 579 190 523" fill="none" stroke="var(--leaf)" stroke-width="5" stroke-linecap="round"/>
<path class="vine" d="M331 543 C412 519 444 462 438 384" fill="none" stroke="var(--leaf)" stroke-width="5" stroke-linecap="round"/>
<path d="M188 516 C138 491 127 446 164 417 C220 430 244 470 219 513 C209 520 199 522 188 516Z" fill="url(#leafGrad)" opacity=".9"/>
<path d="M432 372 C493 360 535 390 533 439 C482 463 435 451 415 405 C417 391 423 381 432 372Z" fill="url(#leafGrad)" opacity=".82"/>
<path d="M286 676 C236 651 226 604 263 576 C319 590 344 631 317 673 C307 680 296 682 286 676Z" fill="url(#leafGrad)" opacity=".78"/>"""


def sparkles() -> str:
    return """<g opacity=".72"><circle cx="116" cy="229" r="7" fill="#fffdf8"/><circle cx="509" cy="153" r="5" fill="#fffdf8"/><circle cx="482" cy="552" r="6" fill="#fffdf8"/><circle cx="148" cy="650" r="4" fill="#fffdf8"/></g>"""


CSS = """
:root {
  --ink: #302733;
  --muted: #746a70;
  --paper: #fffaf4;
  --cream: #fffdf8;
  --petal: #6975ac;
  --petal-deep: #4f5085;
  --sky: #c9dfdd;
  --leaf: #526b4e;
  --leaf-dark: #324531;
  --gold: #c99a4c;
  --line: rgba(82, 107, 78, .18);
  --shadow: 0 22px 60px rgba(48, 39, 51, .14);
  --radius: 8px;
}
* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--ink);
  background: var(--paper);
  font-family: "Avenir Next", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
  line-height: 1.72;
  letter-spacing: 0;
  overflow-x: hidden;
}
a { color: inherit; }
.page {
  min-height: 100svh;
  background:
    linear-gradient(180deg, rgba(255, 253, 248, .3), rgba(255, 250, 244, 1) 82%),
    radial-gradient(circle at 16% 10%, color-mix(in srgb, var(--sky) 70%, transparent), transparent 34%),
    radial-gradient(circle at 86% 2%, rgba(236, 219, 182, .7), transparent 28%),
    var(--paper);
}
.hero {
  position: relative;
  display: grid;
  min-height: 100svh;
  isolation: isolate;
  overflow: hidden;
}
.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(180deg, rgba(255, 250, 244, .15), rgba(255, 250, 244, .94) 78%),
    radial-gradient(circle at 50% 28%, rgba(255, 255, 255, .84), transparent 28%);
  z-index: -1;
}
.brand {
  position: absolute;
  top: max(18px, env(safe-area-inset-top));
  left: clamp(18px, 5vw, 44px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  width: 96px;
  height: 42px;
}
.brand img { display: block; width: 100%; height: auto; }
.hero-art {
  position: absolute;
  inset: 0;
  z-index: -2;
  display: grid;
  place-items: center;
  padding: 46px 0 0;
}
.flower-scene {
  width: min(100vw, 680px);
  height: min(88svh, 760px);
  min-height: 560px;
  display: block;
  filter: drop-shadow(0 28px 42px rgba(50, 69, 49, .18));
}
.hero-copy {
  align-self: end;
  width: min(100%, 760px);
  padding: 0 clamp(18px, 5vw, 52px) max(34px, calc(24px + env(safe-area-inset-bottom)));
}
.eyebrow {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  margin: 0 0 14px;
  padding: 6px 12px;
  border: 1px solid rgba(82, 107, 78, .22);
  border-radius: 999px;
  background: rgba(255, 253, 248, .78);
  color: var(--leaf-dark);
  font-size: 13px;
  font-weight: 800;
  backdrop-filter: blur(10px);
}
h1 {
  margin: 0;
  font-family: Georgia, "Noto Serif TC", serif;
  font-size: clamp(43px, 12vw, 88px);
  line-height: .98;
  font-weight: 700;
  letter-spacing: 0;
  color: var(--ink);
  text-wrap: balance;
}
.lead {
  margin: 20px 0 0;
  max-width: 620px;
  color: #4f454d;
  font-size: clamp(18px, 4.5vw, 23px);
  line-height: 1.78;
  font-weight: 500;
}
.scroll-cue {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  margin-top: 26px;
  color: var(--leaf-dark);
  text-decoration: none;
  font-size: 14px;
  font-weight: 800;
}
.scroll-cue span {
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1px solid rgba(82, 107, 78, .28);
  background: rgba(255, 253, 248, .7);
}
section { padding: clamp(34px, 9vw, 84px) clamp(18px, 5vw, 56px); }
.inner { width: min(920px, 100%); margin: 0 auto; }
.section-kicker {
  margin: 0 0 9px;
  color: var(--gold);
  font-size: 13px;
  font-weight: 900;
  letter-spacing: .16em;
}
h2 {
  margin: 0;
  font-family: Georgia, "Noto Serif TC", serif;
  font-size: clamp(29px, 7vw, 52px);
  line-height: 1.18;
  font-weight: 700;
  letter-spacing: 0;
  text-wrap: balance;
}
.poem { background: var(--cream); }
.poem-card {
  padding: clamp(28px, 7vw, 54px);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: rgba(255, 253, 248, .86);
  box-shadow: var(--shadow);
}
.poem-text {
  margin: 24px 0 0;
  color: #4d4249;
  font-family: Georgia, "Noto Serif TC", serif;
  font-size: clamp(23px, 5.4vw, 38px);
  line-height: 1.64;
  letter-spacing: 0;
}
.story { background: linear-gradient(180deg, var(--cream), color-mix(in srgb, var(--sky) 34%, #fffdf8)); }
.story-grid {
  display: grid;
  grid-template-columns: minmax(0, .92fr) minmax(0, 1.08fr);
  gap: clamp(22px, 5vw, 46px);
  align-items: start;
}
.story-copy p {
  margin: 0 0 1.12em;
  color: #50474e;
  font-size: clamp(17px, 3.8vw, 20px);
}
.quiet-panel {
  border-left: 3px solid var(--petal);
  padding: 19px 20px;
  border-radius: 0 var(--radius) var(--radius) 0;
  background: rgba(255, 253, 248, .72);
  color: var(--petal-deep);
  font-size: 17px;
  font-weight: 700;
}
.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 22px 0 0;
  padding: 0;
  list-style: none;
}
.chips li {
  padding: 9px 12px;
  border: 1px solid rgba(82, 107, 78, .2);
  border-radius: 999px;
  background: rgba(255, 253, 248, .78);
  color: var(--leaf-dark);
  font-size: 14px;
  font-weight: 800;
}
.gift { background: var(--leaf-dark); color: #fffdf8; }
.gift-card {
  display: grid;
  grid-template-columns: minmax(0, .92fr) minmax(240px, .72fr);
  gap: clamp(22px, 5vw, 42px);
  align-items: center;
  padding: clamp(26px, 7vw, 50px);
  border: 1px solid rgba(255, 253, 248, .18);
  border-radius: var(--radius);
  background: linear-gradient(135deg, rgba(255, 253, 248, .12), transparent 54%), rgba(255, 253, 248, .05);
  box-shadow: 0 24px 70px rgba(0, 0, 0, .18);
}
.gift h2, .gift .section-kicker { color: #fffdf8; }
.gift-copy {
  margin: 20px 0 0;
  color: rgba(255, 253, 248, .84);
  font-size: 18px;
}
.gift-badge {
  min-height: 230px;
  display: grid;
  place-items: center;
  padding: 24px;
  border-radius: var(--radius);
  background: #fffdf8;
  color: var(--leaf-dark);
  text-align: center;
}
.gift-badge strong {
  display: block;
  font-family: Georgia, "Noto Serif TC", serif;
  font-size: clamp(32px, 7vw, 58px);
  line-height: 1.12;
  color: var(--petal-deep);
  letter-spacing: 0;
}
.gift-badge small {
  display: block;
  margin-top: 12px;
  color: var(--muted);
  font-size: 14px;
  line-height: 1.6;
  font-weight: 700;
}
.rules { background: var(--paper); }
.rule-list {
  display: grid;
  gap: 12px;
  margin: 24px 0 0;
  padding: 0;
  list-style: none;
}
.rule-list li {
  padding: 15px 16px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: rgba(255, 253, 248, .76);
  color: #514850;
  font-size: 15px;
}
.store { padding-top: 0; }
.store-card {
  padding: 22px;
  border-radius: var(--radius);
  background: color-mix(in srgb, var(--sky) 36%, #fffdf8);
  border: 1px solid var(--line);
  color: #443b42;
  font-size: 15px;
}
.store-card strong {
  display: block;
  margin-bottom: 8px;
  color: var(--leaf-dark);
  font-size: 18px;
}
.footer {
  padding: 24px 18px calc(28px + env(safe-area-inset-bottom));
  color: var(--muted);
  text-align: center;
  font-size: 12px;
}
@media (max-width: 760px) {
  .flower-scene {
    width: 132vw;
    height: 78svh;
    min-height: 520px;
    transform: translateX(4vw) translateY(-3svh);
  }
  .hero-copy { padding-bottom: max(30px, calc(20px + env(safe-area-inset-bottom))); }
  .story-grid, .gift-card { grid-template-columns: 1fr; }
  .gift-badge { min-height: 190px; }
}
@supports not (color: color-mix(in srgb, red, white)) {
  .page { background: var(--paper); }
  .story { background: var(--cream); }
  .store-card { background: #edf4e8; }
}
@media (prefers-reduced-motion: no-preference) {
  .flower-main { animation: openFlower 1200ms cubic-bezier(.2, .8, .2, 1) both; transform-origin: 52% 34%; }
  .vine { animation: growIn 1200ms ease-out both; transform-origin: 50% 100%; }
  @keyframes openFlower {
    from { opacity: 0; transform: scale(.92) rotate(-2deg); }
    to { opacity: 1; transform: scale(1) rotate(0); }
  }
  @keyframes growIn {
    from { opacity: 0; transform: translateY(24px); }
    to { opacity: 1; transform: translateY(0); }
  }
}
"""


def render(card):
    petal, petal_deep, sky, leaf, leaf_dark, gold = card["palette"]
    css_vars = f"--petal:{petal};--petal-deep:{petal_deep};--sky:{sky};--leaf:{leaf};--leaf-dark:{leaf_dark};--gold:{gold};"
    url = f"{EVENT_URL}/{card['slug']}/"
    chips = "\n".join(f"            <li>{escape(chip)}</li>" for chip in card["chips"])
    rules = "\n".join(f"          <li>{escape(rule)}</li>" for rule in card["rules"])
    story = "\n".join(f"          <p>{escape(p)}</p>" for p in card["story"])
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>妳抽到{escape(card['flower'])}｜ASify 敦化店七月花卡</title>
  <meta name="description" content="ASify 敦化店七月花卡。妳抽到{escape(card['flower'])}：{escape(card['meaning'])}">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="妳抽到{escape(card['flower'])}｜ASify 敦化店七月花卡">
  <meta property="og:description" content="{escape(card['lead'])}">
  <style>{CSS}</style>
</head>
<body>
  <main class="page" style="{css_vars}">
    <header class="hero">
      <a class="brand" href="../" aria-label="ASify 七月敦化店花卡活動">
        <img src="{LOGO}" alt="ASify">
      </a>
      <div class="hero-art" aria-hidden="true">
        <svg class="flower-scene" viewBox="0 0 640 760" role="img">
          <defs>
            <radialGradient id="petalGrad" cx="52%" cy="38%" r="62%">
              <stop offset="0%" stop-color="#fffdf8"/>
              <stop offset="42%" stop-color="var(--petal)"/>
              <stop offset="100%" stop-color="var(--petal-deep)"/>
            </radialGradient>
            <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="color-mix(in srgb, var(--leaf) 62%, #fffdf8)"/>
              <stop offset="100%" stop-color="var(--leaf)"/>
            </linearGradient>
          </defs>
          {flower_svg(card['svg'])}
        </svg>
      </div>
      <div class="hero-copy">
        <p class="eyebrow">七月敦化店花卡｜妳抽到{escape(card['flower'])}</p>
        <h1>{escape(card['title'])}</h1>
        <p class="lead">{escape(card['lead'])}</p>
        <a class="scroll-cue" href="#gift"><span>↓</span>看看今天這張卡帶來什麼</a>
      </div>
    </header>

    <section class="poem" id="meaning">
      <div class="inner">
        <article class="poem-card">
          <p class="section-kicker">FLOWER LANGUAGE</p>
          <h2>{escape(card['flower'])}的花語</h2>
          <p class="poem-text">{escape(card['meaning'])}</p>
        </article>
      </div>
    </section>

    <section class="story" id="story">
      <div class="inner story-grid">
        <div>
          <p class="section-kicker">ASIFY STORY</p>
          <h2>{escape(card['story_title'])}</h2>
        </div>
        <div class="story-copy">
{story}
          <div class="quiet-panel">{escape(card['note'])}</div>
          <ul class="chips" aria-label="適合逛的品項">
{chips}
          </ul>
        </div>
      </div>
    </section>

    <section class="gift" id="gift">
      <div class="inner gift-card">
        <div>
          <p class="section-kicker">TODAY'S CARD GIFT</p>
          <h2>今日花卡禮物</h2>
          <p class="gift-copy">{escape(card['gift_copy'])}</p>
        </div>
        <div class="gift-badge" aria-label="{escape(card['gift'].replace('<br>', ''))}">
          <div>
            <strong>{card['gift']}</strong>
            <small>請出示實體花卡與此頁面給店員確認</small>
          </div>
        </div>
      </div>
    </section>

    <section class="rules" id="rules">
      <div class="inner">
        <p class="section-kicker">CARD RULES</p>
        <h2>使用規則</h2>
        <ul class="rule-list">
{rules}
        </ul>
      </div>
    </section>

    <section class="store">
      <div class="inner">
        <div class="store-card">
          <strong>ASify 敦化店</strong>
          台北市大安區忠孝東路四段216巷8弄16號1樓<br>
          捷運忠孝敦化站 3 號出口步行 1 分鐘<br>
          營業時間：週一至週日 12:30-20:30
        </div>
      </div>
    </section>

    <footer class="footer">ASify 七月敦化店花卡活動｜本頁為{escape(card['flower'])}卡專屬 QR 頁</footer>
  </main>
</body>
</html>
"""


def main():
    for card in CARDS:
        target = BASE / card["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(card), encoding="utf-8")
        print(f"{target} -> {EVENT_URL}/{card['slug']}/")


if __name__ == "__main__":
    main()
