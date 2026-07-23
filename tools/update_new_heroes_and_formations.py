from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


new_heroes = r'''
        {
          name: "Aokiji",
          rarity: "UR",
          role: "SUP",
          affinities: ["Marine Admirals", "Logia Fruit", "Marine", "Control", "Ice"],
          status: "complete",
          portrait: "images/heroes/aokiji/hero-aokiji-card-ur.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Soporte de control para equipos Marine/Logia. Congela, reduce recuperacion de energia y castiga objetivos congelados.",
          recommended: {
            dial: "Blue Shell observado en Handbook.",
            weapon: "Iron / Gun segun captura de recomendaciones.",
            gear: "Wind observado como opcion sugerida.",
            image: "images/heroes/aokiji/handbook-aokiji-recommendations.jpeg",
            note: "Buen candidato para acompañar a Akainu o Sengoku cuando necesitas control y limpieza de buffs.",
          },
          stats: {},
          skills: [
            {
              name: "Partisan",
              type: "Activa",
              icon: "images/heroes/skill-icons/aokiji-partisan.jpg",
              summary:
                "Activa de control aleatorio. Golpea a 3 enemigos y puede congelarlos.",
              effects: [
                ["Daño principal", "80% ATK a 3 enemigos aleatorios"],
                ["Control", "25% de probabilidad de aplicar Frozen durante 1 turno"],
                ["Frozen", "estado de control que impide moverse al objetivo"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Fragility",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/aokiji-fragility.jpg",
              summary:
                "Aumenta el castigo sobre enemigos congelados.",
              effects: [
                ["Contra Frozen", "al atacar objetivos congelados aumenta el daño recibido por ellos en 25%"],
                ["Duracion", "2 turnos"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Ice Time",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/aokiji-ice-time.jpg",
              summary:
                "Mejora Partisan con dispersion de buffs y mas daño contra enemigos con reduccion de energia.",
              effects: [
                ["Disperse", "Partisan elimina 1 buff del objetivo"],
                ["Contra Energy Restoration reduce", "elimina 1 buff adicional y aumenta el daño causado en 28%"],
                ["Disperse", "quita efectos positivos del objetivo"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Frost Blade",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/aokiji-frost-blade.jpg",
              summary:
                "Convierte el ataque normal en control y reduccion de recuperacion de energia.",
              effects: [
                ["Ataque normal", "reduce la recuperacion de energia del objetivo en 50% durante 2 turnos"],
                ["Control", "100% de probabilidad de aplicar Frozen durante 1 turno al golpear"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Frigid Capsule",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/aokiji-frigid-capsule.jpg",
              summary:
                "Seguro defensivo cuando Aokiji queda bajo de vida.",
              effects: [
                ["Condicion", "cuando su HP baja de 30%"],
                ["Contraataque de control", "100% de probabilidad de congelar al atacante"],
                ["Curacion", "recibe Healing equivalente a 28% HP"],
                ["Limite", "se activa 1 vez por batalla"],
              ],
            },
          ],
        },
        {
          name: "Sengoku",
          rarity: "UR",
          role: "DEF",
          affinities: ["Marine Marshall", "Zoan Fruit", "Marine", "Tank", "Shield"],
          status: "complete",
          portrait: "images/heroes/sengoku/hero-sengoku-card-ur.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Tanque Marine con escudo propio, reduccion de daño y soporte a Marine Admirals.",
          recommended: {
            dial: "Blue defensive dial observado.",
            weapon: "Iron recomendado en captura.",
            gear: "Defend gear observado.",
            image: "images/heroes/sengoku/handbook-sengoku-recommendations.jpeg",
            note: "La captura de comentarios lo marca como muy buen DEF; encaja delante de Aokiji y Akainu.",
          },
          stats: {},
          skills: [
            {
              name: "Sengoku the Buddha",
              type: "Activa",
              icon: "images/heroes/skill-icons/sengoku-the-buddha.jpg",
              summary:
                "Activa defensiva: pega a todos y se coloca escudo.",
              effects: [
                ["Daño principal", "70% ATK a todos los enemigos"],
                ["Escudo", "gana shield equivalente a 100% ATK"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Powerful Shield",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/sengoku-powerful-shield.jpg",
              summary:
                "Hace que sus escudos rindan mucho mas.",
              effects: [
                ["Con shield activo", "reduce el daño recibido en 30%"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Justice",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/sengoku-justice.jpg",
              summary:
                "Escala mejor si el equipo incluye Marine Admirals.",
              effects: [
                ["Con Marine Admirals aliados", "+10% DMG Reduction propio"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Top Command",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/sengoku-top-command.jpg",
              summary:
                "Buffea el combo de los Marine Admirals despues de usar la activa.",
              effects: [
                ["Tras Sengoku the Buddha", "+15% Combo Rate a Marine Admirals aliados"],
                ["Duracion", "2 turnos"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Deterrence the Buddha",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/sengoku-deterrence-the-buddha.jpg",
              summary:
                "Debuff defensivo al recibir ataques.",
              effects: [
                ["Al ser atacado", "40% de probabilidad de reducir el skill damage del atacante en 15%"],
                ["Duracion", "1 turno"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
          ],
        },
        {
          name: "Caesar",
          rarity: "UR",
          role: "SUP",
          affinities: ["Scientist", "Punk Hazard", "Logia Fruit", "Control", "Gas"],
          status: "partial",
          portrait: "images/heroes/caesar/hero-caesar-card-ur.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Soporte de control con Confusion, Vulnerable y mejoras cuando sus ataques son esquivados.",
          recommended: {
            dial: "Blue support dial observado.",
            weapon: "Gear/weapon defensivo visto en la ficha.",
            gear: "Recomendacion pendiente de traducir completa.",
            image: "images/heroes/caesar/handbook-caesar-recommendations.jpeg",
          },
          stats: {},
          skills: [
            {
              name: "Slime Ball",
              type: "Activa",
              icon: "images/heroes/skill-icons/caesar-slime-ball.jpg",
              summary:
                "Daño a todos los enemigos con probabilidad de Confusion.",
              effects: [
                ["Daño principal", "60% ATK a todos los enemigos"],
                ["Control", "30% de probabilidad de aplicar Confusion durante 1 turno"],
                ["Confusion", "el objetivo tiene chance de golpear aliados"],
              ],
            },
            {
              name: "Fragile Illusion",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/caesar-fragile-illusion.jpg",
              summary:
                "Castiga objetivos bajo control.",
              effects: [
                ["Contra Control", "aplica 25% Vulnerable durante 2 turnos"],
              ],
            },
            {
              name: "Candyman",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/caesar-candy-wall.jpg",
              summary:
                "Si le esquivan el ataque normal, sube su control.",
              effects: [
                ["Al fallar/dodge del ataque normal", "+20% Control Rate durante 2 turnos"],
              ],
            },
          ],
        },
        {
          name: "Tsuru",
          rarity: "UR",
          role: "SUP",
          affinities: ["Marine", "Marine Staff", "Superman Fruit", "Paramecia", "Healer"],
          status: "partial",
          portrait: "images/heroes/tsuru/hero-tsuru-card-ur.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Soporte Marine de limpieza, curacion y proteccion. Las capturas muestran vulnerabilidad enemiga y mejoras defensivas aliadas.",
          recommended: {
            dial: "Blue support dial observado.",
            weapon: "Weapon Match visible en captura.",
            gear: "Gear defensivo/soporte observado.",
            image: "images/heroes/tsuru/handbook-tsuru-recommendations.jpeg",
          },
          stats: {},
          skills: [
            {
              name: "Mind Cleansing",
              type: "Activa",
              icon: "images/heroes/skill-icons/tsuru-mind-cleansing.jpg",
              summary:
                "Activa mixta: daña enemigos y cura aliados con menor vida.",
              effects: [
                ["Daño principal", "240% ATK a 3 enemigos aleatorios"],
                ["Curacion", "cura a 3 aliados de menor HP por un valor basado en ATK"],
                ["Nota", "el porcentaje de curacion exacto necesita una captura mas nitida"],
              ],
            },
            {
              name: "Traces of Heart",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/tsuru-traces-of-heart.jpg",
              summary:
                "Despues de Mind Cleansing refuerza a aliados bajos de vida.",
              effects: [
                ["Tras la activa", "aumenta DMG Reduction de 2 aliados de menor HP en 18%"],
                ["Duracion", "2 turnos"],
              ],
            },
            {
              name: "Wash Wash Fruit",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/tsuru-wash-wash-fruit.jpg",
              summary:
                "Añade Vulnerable a los objetivos de Mind Cleansing.",
              effects: [
                ["Objetivos de Mind Cleansing", "reciben 20% Vulnerable durante 2 turnos"],
              ],
            },
          ],
        },
        {
          name: "Shiki",
          rarity: "UR",
          role: "ATK",
          affinities: ["Legendary", "Pirate", "No.1 Swordsman", "Control", "Flying Pirate"],
          status: "partial",
          portrait: "images/heroes/shiki/hero-shiki-card-ur.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Atacante de combo. Sus pasivas suben Crit Rate, Combo Rate y sustain cuando sus combos o habilidades interactuan con dodge.",
          recommended: {
            dial: "Dial ofensivo observado.",
            weapon: "Weapon Match visible en captura.",
            gear: "Gear ofensivo observado.",
            image: "images/heroes/shiki/handbook-shiki-recommendations.jpeg",
          },
          stats: {},
          skills: [
            {
              name: "Blood Dye",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/shiki-blood-dye.jpg",
              summary:
                "Mejora Hit Rate y daño de skill durante secuencias de combo.",
              effects: [
                ["Hit Rate", "+10% Hit Rate al cumplir la condicion de la pasiva"],
                ["Durante combo", "+15% skill damage para la siguiente habilidad"],
                ["Nota", "la condicion completa requiere captura mas nitida"],
              ],
            },
            {
              name: "Gravity Blade",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/shiki-gravity-blade.jpg",
              summary:
                "Aumenta Combo Rate y vuelve a escalar si le esquivan.",
              effects: [
                ["Combo", "+15% Combo Rate"],
                ["Si el combo es esquivado", "+15% Combo Rate adicional durante 2 turnos"],
              ],
            },
          ],
        },
        {
          name: "Moria",
          rarity: "SSR",
          role: "SUP",
          affinities: ["Pirate", "Warlord", "Superman Fruit", "Paramecia", "Control"],
          status: "partial",
          portrait: "images/heroes/moria/hero-moria-card-ssr.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Soporte SSR de supervivencia y buffs. Puede ganar Invincible al caer bajo HP y revive una vez.",
          recommended: {
            dial: "Dial de soporte observado.",
            weapon: "Weapon Match visible.",
            gear: "Gear Match visible.",
            image: "images/heroes/moria/handbook-moria-recommendations.jpeg",
          },
          stats: {},
          skills: [
            {
              name: "Shadow Clone",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/moria-shadow-clone.jpg",
              summary:
                "Seguro defensivo cuando baja mucho de vida.",
              effects: [
                ["Condicion", "cuando su HP baja de 40%"],
                ["Efecto", "gana Invincible durante 2 turnos"],
                ["Invincible", "no recibe ataques ni daño"],
              ],
            },
            {
              name: "Nightmare",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/moria-nightmare.jpg",
              summary:
                "Revive una vez despues de morir.",
              effects: [
                ["Al morir", "revive al siguiente turno"],
                ["HP al revivir", "50% HP"],
                ["Limite", "1 vez por batalla"],
              ],
            },
          ],
        },
        {
          name: "Law",
          rarity: "SSR",
          role: "SUP",
          affinities: ["Pirate", "Worst Generation", "Superman Fruit", "Paramecia", "Healer"],
          status: "partial",
          portrait: "images/heroes/law/hero-law-card-ssr.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Soporte SSR con curacion grupal y burst a un objetivo. Muy util para estabilizar peleas largas.",
          recommended: {
            dial: "Support dial observado en captura.",
            weapon: "Weapon Match visible.",
            gear: "Gear Match visible.",
            image: "images/heroes/law/handbook-law-comments.jpeg",
          },
          stats: {},
          skills: [
            {
              name: "Gamma Knife",
              type: "Activa",
              icon: "images/heroes/skill-icons/law-gamma-knife.jpg",
              summary:
                "Gran golpe a un objetivo y curacion para todo el equipo.",
              effects: [
                ["Daño principal", "600% ATK a 1 enemigo"],
                ["Curacion", "cura a todos los aliados por 60% ATK"],
                ["Nivel mostrado", "Max Level"],
              ],
            },
            {
              name: "Room",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/law-room.jpg",
              summary:
                "Buff inicial de precision para el equipo.",
              effects: [
                ["Inicio de batalla", "+30% Hit Rate a todos los aliados"],
                ["Duracion", "3 rondas"],
              ],
            },
          ],
        },
        {
          name: "Perona",
          rarity: "SSR",
          role: "SUP",
          affinities: ["Pirate", "Thriller Bark", "Superman Fruit", "Paramecia", "Control"],
          status: "partial",
          portrait: "images/heroes/perona/hero-perona-card-ssr.jpeg",
          level: "No visible",
          power: "No visible",
          qualification: "No visible",
          source: "Capturas nuevas de Handbook",
          summary:
            "Soporte de Terror y vulnerabilidad. Buena opcion barata para control si faltan UR completos.",
          recommended: {
            dial: "Support dial observado.",
            weapon: "Weapon Match visible.",
            gear: "Gear Match visible.",
            image: "images/heroes/perona/handbook-perona-recommendations.jpeg",
          },
          stats: {},
          skills: [
            {
              name: "Kage Ghost",
              type: "Activa",
              icon: "images/heroes/skill-icons/perona-kage-ghost.jpg",
              summary:
                "Control en area con probabilidad de Terror.",
              effects: [
                ["Daño principal", "76% ATK a todos los enemigos"],
                ["Control", "35% de probabilidad de aplicar Terror durante 1 turno"],
                ["Terror", "50% de probabilidad de impedir que el objetivo se mueva"],
              ],
            },
            {
              name: "Negative Bomb",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/perona-negative-bomb.jpg",
              summary:
                "La activa añade vulnerabilidad.",
              effects: [
                ["Tras activa", "aplica 15% Vulnerable durante 2 turnos"],
              ],
            },
            {
              name: "Ghost Ghost Boost",
              type: "Pasiva",
              icon: "images/heroes/skill-icons/perona-ghost-ghost-boost.jpg",
              summary:
                "Gana reduccion de daño cuando mueren aliados.",
              effects: [
                ["Al morir un aliado", "+13% DMG Reduction"],
                ["Acumulaciones", "hasta 3 stacks"],
              ],
            },
          ],
        },
'''


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise SystemExit(f"Missing pattern: {old[:80]!r}")
    return text.replace(old, new, 1)


def update_heroes() -> None:
    path = ROOT / "heroes.html"
    text = path.read_text(encoding="utf-8")
    if 'name: "Aokiji"' not in text:
        marker = "\n      ];\n\n      const heroCatalog"
        text = replace_once(text, marker, new_heroes + marker)

    text = text.replace("20 fichas completas", "22 fichas completas · 6 parciales")
    text = text.replace(
        "Usa los filtros para comparar carries, afinidades y fichas completas.",
        "Usa los filtros para comparar carries, tanques, soportes, afinidades y fichas completas o parciales.",
    )
    fixes = {
        "curaci?n": "curación",
        "Curaci?n": "Curación",
        "núcleo": "núcleo",
        "Ya est?": "Ya está",
        "h?roe": "héroe",
    }
    for old, new in fixes.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("20 fichas completas", "28 fichas registradas")
    text = text.replace("Equipos de 2 adelante y 3 atrás", "Equipos de 2 adelante y 3 atrás")
    path.write_text(text, encoding="utf-8")


def update_formations() -> None:
    path = ROOT / "formaciones.html"
    text = path.read_text(encoding="utf-8")

    additions = '''        { id: "sengoku", name: "Sengoku", role: "DEF", portrait: "images/heroes/sengoku/hero-sengoku-card-ur.jpeg", tags: ["Marine", "Marine Marshall", "Zoan Fruit"] },
        { id: "aokiji", name: "Aokiji", role: "SUP", portrait: "images/heroes/aokiji/hero-aokiji-card-ur.jpeg", tags: ["Marine", "Marine Admirals", "Logia Fruit", "Control"] },
        { id: "tsuru", name: "Tsuru", role: "SUP", portrait: "images/heroes/tsuru/hero-tsuru-card-ur.jpeg", tags: ["Marine", "Superman Fruit", "Paramecia", "Healer"] },
        { id: "shiki", name: "Shiki", role: "ATK", portrait: "images/heroes/shiki/hero-shiki-card-ur.jpeg", tags: ["Legendary", "Pirate", "No.1 Swordsman"] },
        { id: "caesar", name: "Caesar", role: "SUP", portrait: "images/heroes/caesar/hero-caesar-card-ur.jpeg", tags: ["Scientist", "Logia Fruit", "Control"] },
        { id: "moria", name: "Moria", role: "SUP", portrait: "images/heroes/moria/hero-moria-card-ssr.jpeg", tags: ["Pirate", "Warlord", "Paramecia", "Control"] },
        { id: "law", name: "Law", role: "SUP", portrait: "images/heroes/law/hero-law-card-ssr.jpeg", tags: ["Pirate", "Worst Generation", "Paramecia", "Healer"] },
        { id: "perona", name: "Perona", role: "SUP", portrait: "images/heroes/perona/hero-perona-card-ssr.jpeg", tags: ["Pirate", "Thriller Bark", "Paramecia", "Control"] },
'''
    if '{ id: "sengoku"' not in text:
        text = replace_once(text, '        { id: "", name: "Ranura abierta", role: "OPEN", portrait: "", tags: [] },\n', '        { id: "", name: "Ranura abierta", role: "OPEN", portrait: "", tags: [] },\n' + additions)

    start = text.index("      const defaultFormations = [")
    end = text.index("\n      const storageKey", start)
    replacement = r'''      const defaultFormations = [
        {
          name: "Daño crítico estable",
          purpose: "Arena / progreso general",
          front1: "kaido",
          front2: "sengoku",
          back1: "big-mom",
          back2: "rayleigh",
          back3: "marco",
          notes:
            "Doble frente resistente para que Big Mom y Rayleigh tengan turnos. Marco sostiene con curación y resurrección.",
          advice:
            "Usala cuando no sabes qué vas a enfrentar. Si te falta daño, cambia Marco por Akainu; si te falta aguante, deja a Marco y sube prioridad de gear DEF en los frontales.",
        },
        {
          name: "Big Mom Band",
          purpose: "Sinergia de banda",
          front1: "sengoku",
          front2: "smoothie",
          back1: "big-mom",
          back2: "katakuri",
          back3: "cracker",
          notes:
            "Big Mom, Katakuri, Cracker y Smoothie activan el núcleo Big Mom Band. Sengoku entra como tanque externo porque todavía falta confirmar otro frontal perfecto de la banda.",
          advice:
            "Big Mom debe ser el carry mejor equipado. Katakuri y Cracker aportan daño constante; Smoothie ayuda a sostener. Si desbloqueas un tanque Big Mom Band fuerte, reemplaza a Sengoku.",
        },
        {
          name: "Legendarios",
          purpose: "Núcleo Legendary / peleas largas",
          front1: "kaido",
          front2: "sengoku",
          back1: "rayleigh",
          back2: "shiki",
          back3: "otohime",
          notes:
            "Rayleigh y Shiki dan presión ofensiva Legendary. Kaido y Sengoku absorben; Otohime aporta soporte para alargar la pelea.",
          advice:
            "Buena para probar daño de carries caros. Rayleigh necesita stats ofensivas; Shiki funciona mejor si el equipo aguanta suficientes turnos para aprovechar combo y crit.",
        },
        {
          name: "Marines",
          purpose: "Marine / Logia",
          front1: "sengoku",
          front2: "",
          back1: "akainu-new-world",
          back2: "aokiji",
          back3: "tsuru",
          notes:
            "Sengoku activa defensa y bonifica Marine Admirals. Akainu aporta daño, Aokiji control y Tsuru curación/limpieza.",
          advice:
            "Usala contra equipos que dependen de buffs o de moverse primero. Aokiji congela y dispersa; Sengoku compra tiempo para que Akainu limpie. La segunda ranura frontal queda editable para tu mejor DEF.",
        },
        {
          name: "Control económico",
          purpose: "SSR / control y sustain",
          front1: "moria",
          front2: "bartolomeo",
          back1: "law",
          back2: "perona",
          back3: "caesar",
          notes:
            "Formación de control con SSR y soportes: Moria sobrevive, Bartolomeo protege, Law cura, Perona aplica Terror y Caesar añade Confusion/Vulnerable.",
          advice:
            "Ideal para probar alternativas si no tienes todos los UR subidos. No busca explotar daño máximo: busca negar turnos, sobrevivir y ganar por desgaste.",
        },
        {
          name: "Boss / daño máximo",
          purpose: "Boss / rankings de daño",
          front1: "kaido",
          front2: "",
          back1: "big-mom",
          back2: "katakuri",
          back3: "akainu-new-world",
          notes:
            "Tres carries fuertes para medir daño bruto. Kaido intenta sostener el frente; la segunda ranura queda libre para tu mejor tanque o buff real.",
          advice:
            "Usala en Boss si el equipo no muere demasiado rápido. Si cae antes de rotar habilidades, cambia un carry por Marco, Tsuru o Law y compara el daño total, no solo el daño por turno.",
        },
      ];
'''
    text = text[:start] + replacement + text[end:]

    text = text.replace('<div class="formation-notes"></div>', '<div class="formation-notes"></div>\n        <div class="formation-advice"></div>')
    text = text.replace('card.querySelector(".formation-notes").textContent = formation.notes || "Notas pendientes.";','card.querySelector(".formation-notes").textContent = formation.notes || "Notas pendientes.";\n          card.querySelector(".formation-advice").textContent = formation.advice ? `Consejo: ${formation.advice}` : "Consejo: pendiente de pruebas.";')
    text = text.replace('notes: editor.elements.notes.value.trim(),','notes: editor.elements.notes.value.trim(),\n              advice: current[index].advice || "",')
    text = text.replace('const storageVersion = "2";', 'const storageVersion = "3";')
    text = text.replace('Ya est? usado', 'Ya está usado')
    text = text.replace('AtrÃ¡s', 'Atrás').replace('DaÃ±o', 'Daño').replace('formaciÃ³n', 'formación').replace('FormaciÃ³n', 'Formación').replace('hÃ©roe', 'héroe')
    path.write_text(text, encoding="utf-8")


def update_css() -> None:
    path = ROOT / "index.css"
    text = path.read_text(encoding="utf-8")
    if ".formation-advice" not in text:
        text += r'''

.formation-advice {
  margin-top: 10px;
  padding: 12px 14px;
  color: #23303f;
  font-size: 0.9rem;
  line-height: 1.55;
  background: #fff7df;
  border: 1px solid #d7bc79;
  border-left: 4px solid #a87425;
  border-radius: 3px;
}
'''
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_heroes()
    update_index()
    update_formations()
    update_css()


if __name__ == "__main__":
    main()
