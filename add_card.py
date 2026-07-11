import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the last prompt card
prompts = list(re.finditer(r'<article class="glass-card prompt-card"[\s\S]*?</article>', html))
if prompts:
    last_prompt = prompts[-1]
    end_pos = last_prompt.end()

    new_prompt = """
            <article class="glass-card prompt-card" data-category="prompt" data-tags="couple">
                <div class="prompt-img-wrapper">
                    <img src="https://i.postimg.cc/3wZq3461/Two-people-eating-donuts-2K-202607111651.jpg" alt="Prompt" class="card-img prompt-img" data-prompt="STYLE:

CAMERA_AND_ANGLE: Medium shot, eye-level camera, straight horizontal axis.

COLOR_AND_LIGHTING: Warm, slightly greenish-yellow ambient lighting. Distinct, relatively harsh cast shadows falling directly onto the wall behind the figures and onto the floor, suggesting a strong localized light source. Natural balanced color palette — neutral skin tones with healthy warmth, no color cast.

BACKGROUND_AND_ENVIRONMENT: Casual indoor room interior. A simple wall with a low baseboard meeting the floor. The wall is casually decorated with taped-up posters, including one depicting a silhouette playing a guitar. An electrical outlet with a plugged-in white cord is visible on the right side of the wall. An open, flat cardboard box holding a donut rests on the floor to the left, while a tall, dark green energy drink can stands on the floor to the right. 

FIGURE 1:

Position & Gravity: Sitting directly on the floor on the left side of the frame, leaning its upper back comfortably against the wall. Weight is firmly distributed between the pelvis on the floor and the upper back against the vertical surface.

Head & Expression: Head tilted slightly down and turned slightly inward toward the center. A wide, relaxed, and cheerful smile, with eyes visibly squinting in an expression of quiet happiness.

Anatomical Mapping: Torso leaning back. Right arm raised and bent outward at the elbow, hand holding a donut suspended near its face. Left arm extended downward, hand resting loosely on the floor near the cardboard box. Both legs extended forward with knees slightly bent.

Clothing & Gear: A ribbed knit beanie hat, large thin-rimmed eyeglasses, a loose, oversized dark short-sleeved t-shirt with a blue rectangular graphic design on the chest, and baggy green pants.

FIGURE 2:

Position & Gravity: Sitting directly on the floor on the right side of the frame, adjacent to Figure 1. Torso leaning its upper back heavily against the wall behind it. Posture is slouched and highly relaxed.

Head & Expression: Head tilted backward and angled slightly upward. Mouth wide open in the middle of taking a bite. Eyes half-closed in an expression of dramatic, relaxed enjoyment.

Anatomical Mapping: Torso leaning backward. Left arm raised high and bent, hand bringing a donut directly to its open mouth. Right arm extended downward, palm resting flat on the floor to brace and support its leaning weight. Right leg extended forward, left leg bent with the knee raised.

Clothing & Gear: A tight-fitting white ribbed tank top, thick layered silver chain necklaces, thin bracelets on the left wrist, and extremely distressed, baggy blue denim jeans with massive jagged rips across the knees and thighs.

INTERACTION: The figures sit closely side-by-side. Figure 2's right hand rests flat on the ground immediately next to Figure 1's left side, nearly touching. Their cast shadows overlap and interact on the wall directly behind their shoulders, grounding both figures securely in the shared physical space.

FORMAT: 4/3

[CRITICAL: The reference image(s) above show the EXACT appearance of the character(s).]">
                    <button class="copy-prompt-btn" title="Копировать промпт">
                        <svg class="svg-icon" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    </button>
                </div>
            </article>"""

    html = html[:end_pos] + new_prompt + html[end_pos:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully added new prompt card.")
else:
    print("Could not find any prompt cards to append after.")
