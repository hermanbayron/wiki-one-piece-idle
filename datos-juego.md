# Datos del juego

Este archivo guarda los datos observados en capturas para construir la wiki de
One Piece Idle Pirate. Separar lo observado de lo inferido ayuda a no inventar
reglas del juego sin confirmarlas.

## Jugador principal observado

- Nombre: Hides
- Nivel: Lv.230
- VIP: V6
- Poder en ciudad: 1424384169
- Poder en Arena: 1.4B
- Oro visible: 15.2M
- Diamantes visibles: 403

## Ciudad principal

Imagen: `images/city/Inicio.jpeg`

Accesos visibles:

- Instance
- Impel Down
- Boss
- Arena
- Altar
- Market
- Trial
- Leaderboard
- Vegapunk's
- Main City
- Hero
- Adventure
- Summon
- Guild
- Quest
- Friends
- Mail
- Backpack

Accesos laterales o superiores:

- Festival Event
- Growth Path
- Time-limited Event
- Combo Top-up Gift
- Discount Pack
- 1ST TOP UP GIFT
- 1000 Draws
- Permanently Available
- The Summit War
- Island Survival
- Month Pass
- Perk
- Benefits

## Trial

Imagen: `images/trial/Trial.jpeg`

Pantalla con cuatro pruebas visibles:

- Long Ring Island Adventure: Action 1/15. Personaje destacado: Foxy.
- Supernova Showdown: Action 0/1. Personaje destacado: Trafalgar Law.
- Thriller Bark: Action 20/50. Personaje destacado: Gecko Moria.
- Haki Training Room: Action 0/6. Personaje destacado: Roronoa Zoro.

Observado:

- Hay un boton Return.
- Thriller Bark tiene aviso rojo.
- Los contadores usan el formato Action actual/maximo.
- Long Ring Island Adventure usa tablero con dado, boton Throw, items owned y
  un boton Prevent.
- Long Ring Island Adventure muestra moneda 100, Attempts 1/15 antes de tirar
  y 0/15 despues de tirar, con timer alrededor de 01:43.
- Supernova Showdown muestra mapa de stages con nodos Defeated, moneda azul
  1100, Raid con coste 400, Revive y Supernova Store.
- Thriller Bark muestra Floor 114, boton Reset Map, Remaining 3/50, cofres
  restantes y timer 00:02:26.
- Haki Training Room muestra Start, Attempts 0/6, timer 02:25:22 y Rewards
  Preview con Haoshoku, Busoshoku, Kenbunshoku y Basic Pluck.
- Long Ring Island Adventure es un tablero con dado. Throw consume intento,
  mueve por casillas y puede apoyarse en items owned como dado especial, cañon
  y Prevent.
- Supernova Showdown funciona por mapa de stages; los nodos completados quedan
  como Defeated. El lateral muestra stages pares 4, 6, 8 y 10.
- Thriller Bark funciona por pisos. En la captura esta en Floor 114, tiene
  energia/Remaining, cofres restantes, enemigos visibles y Reset Map 1 vez.
- Haki Training Room parece una prueba de timing/barra: Rewards Preview usa los
  colores rojo, amarillo, azul y verde para Haoshoku, Busoshoku, Kenbunshoku y
  Basic Pluck.

Imagenes internas nuevas:

- `images/trial/trial-long-ring-board-before-throw.jpeg`
- `images/trial/trial-long-ring-board-after-throw.jpeg`
- `images/trial/trial-supernova-showdown-map.jpeg`
- `images/trial/trial-thriller-bark-floor-114.jpeg`
- `images/trial/trial-haki-training-room.jpeg`

Inferido pendiente de confirmar:

- Trial parece funcionar como un conjunto de desafios o pruebas diarias.
- Las acciones podrian reiniciarse por dia o por evento.

## Instance

Imagenes fuente:

- `images/instance/instance-menu.jpeg`
- `images/instance/instance-resource-exp-stage-37.jpeg`
- `images/instance/instance-resource-breakthrough-stage-37.jpeg`
- `images/instance/instance-resource-forge-stone-stage-35.jpeg`
- `images/instance/instance-resource-enhance-stone-stage-35.jpeg`
- `images/instance/instance-resource-crystal-dust-stage-34.jpeg`
- `images/instance/instance-gear-stage-28.jpeg`
- `images/instance/instance-dial-stage-27.jpeg`
- `images/materials/material-exp-pass.jpeg`
- `images/materials/material-breakthrough-pass.jpeg`
- `images/materials/material-forge-stone.jpeg`
- `images/materials/material-enhance-stone.jpeg`
- `images/materials/material-crystal-dust.jpeg`
- `images/materials/material-refine-stone.jpeg`

Datos observados:

- Instance tiene tres entradas principales: Resource Instance, Gear Instance y
  Dial Instance.
- En el menu cada entrada muestra `0 times remaining`.
- En las pantallas internas aparece boton `Raid`.
- Intentos visibles: `Attempts: 0/2`.
- Recursos visibles en estas capturas: oro 13.5M y diamantes 3445.
- Resource Instance tiene pestanas inferiores: Exp, Breakthrough, Forge Stone,
  Enhance Stone y Crystal Dust.
- Exp Instance muestra Stage 36 -> Stage 37 y recompensa visible 508.6K + EXP
  5100.
- Breakthrough muestra Stage 36 -> Stage 37 y recompensa visible 15.5K + EXP
  5100.
- Forge Stone muestra Stage 34 -> Stage 35 y recompensa visible 11.8K + EXP
  5160.
- Enhance Stone muestra Stage 34 -> Stage 35 y recompensa visible 15.6K + EXP
  5160.
- Crystal Dust muestra Stage 33 -> Stage 34 y recompensa visible 13.7K + EXP
  5160.
- Gear Instance muestra Stage 27 -> Stage 28 y Pass Reward con dos piezas de
  equipo.
- Dial Instance muestra Stage 26 -> Stage 27 y Loot today con tres diales.
- Hay stages bloqueados con candado, por ejemplo 35, 36 o 38 segun pestana.
- Los intentos diarios base son 2.
- En instancias basicas se pueden comprar intentos extra por 60 gemas, hasta
  dos compras. Luego aparece un intento extra de 120 gemas.
- En Gear Instance y Dial Instance el intento extra cuesta 120 gemas
  directamente.
- EXP Pass se usa junto con oro para subir niveles de heroes.
- Breakthrough Pass se usa para subir limites de nivel en 20, 40, 60, 80, 100
  y luego cada 10 niveles.

Lectura:

- Instance parece ser el modo de farmeo diario de materiales concretos.
- Resource Instance se elige segun la mejora que necesites: experiencia,
  breakthrough, forge stone, enhance stone o crystal dust.
- Gear Instance y Dial Instance son ramas separadas, no una sola instancia de
  equipo.
- Gear Instance sirve para obtener piezas o materiales de gear/equipo.
- Dial Instance sirve para obtener diales o materiales asociados a diales.
- Las tres ramas principales de Instance funcionan como farmeo de materiales:
  Resource para recursos generales, Gear para equipo y Dial para diales.
- Subir de stage probablemente mejora la cantidad o calidad de las recompensas.
- Si un heroe queda frenado por limite, no alcanza con EXP Pass y oro:
  tambien hace falta Breakthrough Pass.

## Materiales clasificados

Imagenes fuente:

- `images/materials/material-team-instance-coin.jpeg`
- `images/materials/material-endurance-pass.jpeg`
- `images/materials/material-training-pass.jpeg`
- `images/materials/material-historic-stele.jpeg`
- `images/materials/material-magnet-powder.jpeg`
- `images/materials/material-magnet-stone.jpeg`
- `images/materials/material-haoshoku-pluck.jpeg`
- `images/materials/material-kenbunshoku-pluck.jpeg`
- `images/materials/material-busoshoku-pluck.jpeg`
- `images/materials/material-basic-pluck.jpeg`
- `images/materials/material-terminating-power.jpeg`
- `images/materials/material-terminating-soul.jpeg`
- `images/materials/material-cage-shard.jpeg`
- `images/materials/material-fine-iron.jpeg`

Datos observados:

- Team Instance Coin se cambia por objetos en Team Instance Store.
- Endurance Pass es material de Taijutsu Training; fuentes observadas:
  Idling y Long Ring Island Adventure.
- Training Pass se usa en Potential, desbloqueado tras despertar el heroe a 3
  estrellas; fuentes observadas: Thriller Bark y Market.
- Historic Stele sirve para reclutar heroes SR o SSR en Tree of Knowledge,
  desbloqueado en Lv.60.
- Magnet Powder y Magnet Stone son materiales de Compass. Powder mejora,
  Stone avanza.
- Haoshoku, Kenbunshoku, Busoshoku y Basic Pluck se usan como coste de
  habilidades Haki de enemigos.
- Fine Iron es material de subida de estrellas de weapon; fuente observada:
  Sea Train y Weapon dissolve.
- Terminating Power mejora Finishing Move.
- Terminating Soul se usa para Reshape de Finishing Move.
- Cage Shard junta 100 fragmentos para componer Finishing Move - Cage.

## Market

Imagenes fuente:

- `images/market/market-common-market.jpeg`
- `images/market/market-vip-market.jpeg`
- `images/city/city-market-store-map.jpeg`

Datos observados:

- Market aparece como acceso en la ciudad.
- Tiene Common Market y VIP Market.
- Recursos visibles: oro 13.5M y diamantes 3445.
- Common Market muestra Refresh con coste 20 diamantes y timer 00:43:54.
- VIP Market muestra Free Refresh (5).
- Hay compras con oro y con diamantes.
- Hay productos con descuentos 30% y 50% off.
- Hay productos Sold Out.
- Se observan fragmentos SSR/SR, materiales, diales/recursos y objetos con
  cantidades como 4680, 888, 150, 100, 50 y x10.
- Common Market parece mejor para recursos basicos y compras con oro.
- VIP Market concentra objetos mas raros, fragmentos SSR/SR y materiales que
  normalmente cuestan diamantes.
- Usar Free Refresh de VIP antes de gastar diamantes parece eficiente.
- En Common Market conviene esperar timer o comprar solo ofertas claras antes
  de pagar refresh por 20 diamantes.

## Boss

Imagenes fuente:

- `images/boss/Boss.jpeg`
- `images/boss/boss-contest-low-level-list.jpeg`
- `images/boss/boss-contest-high-level-list.jpeg`
- `images/boss/boss-contest-luffy-challenge.jpeg`

Modos visibles:

- Boss Contest: Attempts 0/2.
- Sea Train: Attempts 0/1.
- Voyage Adventure: Attempts 1/5.
- Enemy Incoming: Attempts 2/6.

Boss Contest:

- Usa recurso Scroll, visible `0/2`.
- Lista jefes con vida 100%, Owner, Participants, Challenge y Rewards Preview.
- Jefes visibles: Luffy Lv.40, Zoro Lv.80, Ace Lv.80, Aokiji Lv.120/150,
  Blackbeard Lv.120/150 y Doflamingo Lv.120/150.
- En la captura todos muestran Owner None y Participants 0 Players.
- Challenge consume 1 Scroll.
- 2x Challenge consume 2 Scroll y muestra Multiple Rewards.
- El detalle de Luffy muestra Ownership Reward y DMG Ranking.
- La recompensa del killer del BOSS se envia por mail.
- Las recompensas de ranking de daño tambien se envian por mail.
- Si nadie participa aparece "No players challenge the BOSS".

## Sistemas nuevos detectados

Imagenes fuente:

- `images/boss/boss-contest-low-level-list.jpeg`
- `images/boss/boss-contest-high-level-list.jpeg`
- `images/boss/boss-contest-luffy-challenge.jpeg`
- `images/boss/sea-train-carriage-7.jpeg`
- `images/boss/voyage-adventure-main.jpeg`
- `images/boss/enemy-incoming-cp9.jpeg`
- `images/boss/team-instance-recruit-hall.jpeg`
- `images/boss/team-instance-recruit-panel-hint.jpeg`

Boss Contest:

- Usa recurso Scroll, visible `0/2`.
- Lista jefes como Luffy Lv.40, Zoro Lv.80, Ace Lv.80, Aokiji Lv.120/150,
  Blackbeard Lv.120/150 y Doflamingo Lv.120/150.
- Cada jefe muestra vida 100%, Owner None, Participants 0 Players, Challenge y
  Rewards Preview.
- En detalle de Luffy se ve Challenge x1, 2x Challenge x2, Ownership Reward,
  DMG Ranking y texto de que la recompensa del killer se envia por mail.

Sea Train:

- Se ve `The 66 Train`, `7 Carriage`, Daily Rewards y varios vagones derrotados.
- Boss del vagon con boton Challenge, opcion Skip e Inject Hormone.
- Especialidad visible: Support Counter; aumenta daño 50% contra heroes de tipo
  Support.

Voyage Adventure / Enemy Incoming:

- Voyage Adventure muestra Attempts 0/10, Explore deshabilitado, Friend
  Assistance y aviso Enemy Boat Incoming.
- Enemy Incoming muestra Attempts 0/2, tres enemigos con porcentajes, Reward,
  Leaderboard, DMG Top 5 y Hides en rank 5 con 8% de daño.
- En CP9 aparece mejora para heroes con etiqueta Shichibukai: 50% DMG Boost.

Team Instance:

- Tiene Recruit Hall, Inter-server Team Instance y Personal Team Instance.
- Muestra equipos reclutando miembros con servidores, nivel Meteor Volcano y
  Current Members.
- Recruit Panel muestra Remaining Attempts 0/1, evento Meteor Volcand/Volcano,
  niveles 190/200/220/240 y unlock en Lv.240.
- El hint indica que fallar Personal Team Instance Guide no descuenta intentos.

## Leaderboard

Imagenes fuente:

- `images/leaderboard/leaderboard-power.jpeg`
- `images/leaderboard/leaderboard-level.jpeg`
- `images/leaderboard/leaderboard-stage-board.jpeg`
- `images/leaderboard/leaderboard-contest.jpeg`
- `images/leaderboard/leaderboard-sea-train.jpeg`
- `images/leaderboard/leaderboard-impel-down.jpeg`
- `images/leaderboard/leaderboard-guild-board.jpeg`

Tabs visibles:

- Power Leaderboard.
- Level Leaderboard.
- Stage Board.
- Contest Leaderboard.
- Sea Train Board.
- Impel Down.
- Guild Board.

Datos observados de Hides:

- Power Leaderboard: Hides No. 7, Best Power 1.5B.
- Level Leaderboard: Hides No. 10, Current Level Lv.231.
- Stage Board: Hides No. 6, Current Stage Hell04-35.
- Contest Leaderboard: Hides No. 6, Arena Ranking No. 6.
- Sea Train Board: Hides No. 10, Highest Floor 66.
- Impel Down: Hides No. 7, Highest Floor 1839.
- Guild Board: gremio KINGS No. 1, Guild Level 20.

## Impel Down

Imagenes:

- `images/impel-down/impel-down-stage-1840-pass-reward.jpeg`
- `images/impel-down/impel-down-reward-ssr-shards-10.jpeg`
- `images/impel-down/impel-down-reward-ssr-shards-5.jpeg`
- `images/impel-down/endless-prison-stage-progress.jpeg`

Observado:

- Impel Down normal usa stages y cofres cada 5 niveles visibles: 1840,
  1845, 1850 y 1855.
- En Stage 1840 se observa Whitebeard, Attempts 10/10, Leaderboard y
  Stage Effect.
- Stage Effect observado: al comienzo de la batalla, las unidades aliadas con
  etiqueta Superman Fruit tienen 100% de probabilidad de quedar Frozen por 4
  turnos.
- Regla de shards SSR confirmada: cuando el reward da 10 shards SSR,
  corresponde a niveles 10, 20, 30, etc. Cuando da 5 shards SSR,
  corresponde a niveles 5, 15, 25, etc.
- En la captura de 10 shards SSR tambien aparecen 10 tickets rojos y 5 shards
  UR/Slip.
- En la captura de 5 shards SSR aparecen 10 tickets rojos y 5 shards SSR.
- Endless Prison es submodo separado: empieza recién en nivel de usuario 220,
  usa estrellas, Total Stars 30/180, cofres en 40, 50, 60 y 70 Star(s),
  objetivos de stage e Attempts 0/5.
- Endless Prison da plantas/materiales de creación de medicina.
- Rewards Preview de Endless Prison: Obtain 1 Star(s), 2 Star(s) y 3 Star(s)
  muestran Medicine Herb x2.
- Reward acumulado observado: Total Stars 30/180 da Medicine Herb x60.
- Medicine Herb aparece como Medicine Creation Materials. Metodo de obtención:
  Endless Prison y Vegapunk's Lab. No se puede vender (`Unable to Sell`).

## Vegapunk's

Observado:

- El botón Vegapunk's de la ciudad abre Vegapunk's Lab.
- Dentro aparecen S Lab, SS Lab y SSS Lab.
- Cada lab tiene 10 guardians.
- Al derrotar un guardian se habilitan recompensas idle.
- Para desafiar guardians, el Credit del jugador debe calificar. El Credit
  requerido depende del total de créditos de los héroes en Resonance.
- Cuando se alcanza el máximo de idling rewards, no se generan más recompensas.
- Solo se puede desafiar el siguiente guardian después de derrotar el anterior.
- El intervalo entre dos desafíos es de 10 horas.
- S Lab observado: guardians Lv.100, 103, 106, 109 y 112.
- SS Lab observado: guardians Lv.135, 140, 145, 150 y 155.
- SSS Lab observado: guardians Lv.247, 249, 256, 258 y 260.
- SSS Lab muestra recompensas por idling, botones Collect y Fast-Claim, y
  acceso a Go to Resonance.
- Resonance Hero observado: Total Qualification 7806, Resonance level 41,
  TeamHP +319550 y TeamATK +19910.
- Vegapunk's Lab es una fuente de Medicine Herb junto con Endless Prison.
- Potion Crafting observado dentro de Vegapunk's: consume 1 Medicine Herb y
  8000 oro por craft. Proficiency Lv. 9 (320/2000). Chances visibles:
  ATK 58%, DEF 21%, SUP 21%.

Pendiente:

- Confirmar si el premio extra UR/Slip se mantiene en todos los multiples de
  10 o si cambia por tramo.
- Completar recompensas exactas de cofres de Endless Prison por cantidad de
  estrellas y lista completa de plantas.
- Registrar si los Stage Effects cambian por bloque, enemigo o temporada.

## Arena

Imagen: `images/arena/Arena.jpeg`

Observado:

- Tipo de pantalla: PvP / ranking.
- My Ranking: 2.
- Attempts: 0/5.
- Botones visibles: Leaderboard, Refresh, Record, Reward, Lineup, Arena Store,
  Return.
- La pantalla combina un podio superior y una lista central de rivales.
- Los rivales visibles tienen Ranking, nivel, nombre y poder.
- El jugador actual aparece segundo en el podio: Hides.

Podio visible:

- Ranking 1: ZeroQ8, Lv.250, V15, Power 4.3B.
- Ranking 2: Hides, Lv.230, V6, Power 1.4B.
- Ranking 3: Gertrude, Lv.225, V0, Power 1.1B.

Rivales visibles:

- Ranking 1: ZeroQ8, Lv.250, Power 4317513117.
- Ranking 3: Gertrude, Lv.225, Power parcialmente tapado.
- Ranking 4: AKAME, Lv.222, Power 1154762675.
- Ranking 5: Mofix124, Lv.229, Power 985458317.
- Ranking 6: Schweigi, Lv.227, Power 751833866.

Lectura del sistema:

- Arena parece ser el modo PvP principal del juego.
- El ranking personal se muestra como "My Ranking".
- Los intentos usan formato actual/maximo. En la captura el jugador no tiene
  intentos disponibles: 0/5.
- El boton Refresh probablemente cambia o actualiza la lista de rivales.
- El boton Lineup probablemente permite configurar la formacion usada en Arena.
- Arena Store indica que el modo tiene tienda propia o moneda propia.
- Record y Reward sugieren historial de combates y recompensas de ranking.

Comparacion de poder observada:

- ZeroQ8 tiene 4.3B, muy por encima de Hides con 1.4B.
- AKAME tiene 1154762675, menor que el poder de ciudad de Hides
  (1424384169).
- Mofix124 tiene 985458317, menor que Hides.
- Schweigi tiene 751833866, menor que Hides.
- Gertrude aparece cerca del poder de Hides en podio, 1.1B, pero su poder
  exacto en la lista inferior esta parcialmente tapado.

Inferido pendiente de confirmar:

- Refresh actualiza rivales.
- Record muestra historial de combates.
- Reward muestra recompensas de Arena.
- Lineup configura el equipo defensivo u ofensivo de Arena.
- Arena Store es tienda especifica del modo.
- Confirmar si atacar consume exactamente 1 intento.
- Confirmar si al ganar se intercambia posicion o solo se sube ranking.
- Confirmar duracion de temporadas, reinicio diario y premios por ranking.
- Confirmar moneda usada en Arena Store.

## Imagenes disponibles

- `images/ui/icono.jpg`
- `images/ui/Fondo.jpg`
- `images/city/Inicio.jpeg`
- `images/trial/Trial.jpeg`
- `images/boss/Boss.jpeg`
- `images/arena/Arena.jpeg`
- `images/videos/WhatsApp Video 2026-07-09 at 21.07.13.mp4`

## Video fuente

Imagen/video: `images/videos/WhatsApp Video 2026-07-09 at 21.07.13.mp4`

Observado del archivo:

- Formato: MP4.
- Tamaño aproximado: 7.8 MB.
- Origen del nombre: WhatsApp.
- Duracion extraida con OpenCV: 36.13s.
- FPS extraido con OpenCV: 24.24.
- Capturas seleccionadas: 5 en `images/videos/video-frames/`.

Lectura del video:

- 00.00s: pantalla de carga con Whitebeard.
- 02.97s: combate por turnos iniciado. Interfaz muestra Speed x1,
  Remaining 20 Turn, Quit, Cannot be skipped, Auto y barra 0/175.
- 05.94s: Remaining baja a 19 Turn. Se observan 5 unidades aliadas y
  2 enemigos visibles.
- 14.85s: Remaining 18 Turn. Barra inferior visible en 65/175.
- 23.76s: barra inferior visible en 110/175. Aparece daño numerico
  sobre una unidad aliada.
- 29.70s: Remaining 17 Turn. Barra inferior visible en 135/175.
- 35.64s: animacion especial de Doflamingo.

Combate observado:

- El combate usa turnos restantes como limite.
- Hay control de velocidad, al menos Speed x1.
- Hay boton Auto.
- Hay boton Quit.
- El combate mostrado no puede saltarse: "Cannot be skipped".
- Las unidades tienen nivel visible junto a la barra de vida.
- Las unidades muestran iconos de estados, buffs o debuffs.
- La barra inferior usa formato actual/maximo, observado hasta 135/175.

Pendiente:

- Registrar el orden de navegación del jugador.
- Confirmar reglas visibles de modos, intentos y recompensas.
- Confirmar si la barra 0/175 es energia, furia o medidor de habilidad.
- Identificar nombres exactos de las unidades del combate.

## Combate

Fuente principal: `images/videos/WhatsApp Video 2026-07-09 at 21.07.13.mp4`

Capturas detalladas seleccionadas: 5 en `images/videos/video-frames-1s/`.

Observado:

- La pelea inicia con el texto "Battle Start".
- El combate empieza con Remaining 20 Turn.
- Durante el video el contador baja a 19, 18 y 17 turnos.
- Se ven 5 unidades aliadas contra 2 enemigos visibles.
- Cada unidad muestra nivel y barra de vida.
- La interfaz muestra Speed x1 y en un frame se observa Speed x2.
- Hay boton Auto en la esquina inferior derecha.
- Hay boton Quit en la esquina superior derecha.
- Aparece "Cannot be skipped", por lo que esta pelea no se puede saltar.
- La barra inferior arranca en 0/175 y sube a 25/175, 65/175, 95/175,
  110/175 y 135/175.
- Hay iconos de estado sobre aliados y enemigos: iconos verdes, rojos,
  espadas y simbolos de control.
- Se observan numeros de daño grandes al recibir golpes.
- Se observa un ataque de area enemigo que golpea a varias unidades aliadas.
- Se observa texto "Block", indicando bloqueo o mitigacion.
- El final del video muestra una animacion especial de Doflamingo.

Lectura:

- El sistema parece ser combate por turnos con limite de turnos.
- Las acciones cargan una barra inferior con maximo 175.
- La barra podria estar relacionada con energia, furia o habilidad especial.
- Los estados son importantes para interpretar buffs, debuffs, control y daño.
- Algunas habilidades usan animacion a pantalla completa.

Pendiente:

- Confirmar si la barra 175 es individual, global o de habilidad del equipo.
- Confirmar si el orden de turno depende de velocidad, posicion o estadisticas.
- Identificar cada icono de estado.
- Identificar todos los personajes del equipo y enemigos.
- Confirmar si Speed x2 se desbloquea por VIP, nivel o configuracion general.

## Video fuente 2

Imagen/video: `images/videos/WhatsApp Video 2026-07-09 at 22.19.51.mp4`

Observado del archivo:

- Formato: MP4.
- Tamaño aproximado: 22.9 MB.
- Duracion extraida con OpenCV: 99.07s.
- FPS extraido con OpenCV: 24.25.
- Capturas seleccionadas del video: 12 en `images/videos/video2-frames-2s/`.

Lectura del video:

- 00.00s: oferta emergente de skin SSR Luffy Dressrosa. Texto visible:
  "Powerfull Distinctive", "Top up $4.99 to get Luffy's skin", precio $4.99.
- 03.96s: pantalla Adventure/campaña. Capitulo visible:
  Hell04-21 Merciless Death Match III. Boton Challenge Boss.
- 07.92s: recompensa idle acumulada. Idling time: 03:08:02.
- 07.92s: recompensas visibles: oro 573.9K, recurso verde 459.2K,
  recurso violeta 11.5K, diamante/recurso azul 1375 y loot aleatorio.
- 07.92s: Idling Efficiency visible: oro 183139/hr, EXP 161467/hr,
  recurso azul 146511/hr, recurso violeta 3663/hr.
- 07.92s: mensaje inferior: subir a VIP7 aumenta beneficios de Idling
  Efficiency en 30%.
- 13.86s: Common Summon. Puede ganar SR como maximo. Tiene Summon x1,
  Summon x10 y temporizador gratis.
- 19.80s: Advanced Summon. Tickets rojos 262, diamantes 403, Wishlist,
  Rewards Preview, Grants SSR y barra 70/800.
- 19.80s: Advanced Summon indica que 10x Summon garantiza SR Hero.
- 23.76s: resultado de summon: fragmentos de Kuro x80.
- 27.72s: menu Summon con Common Summon, Advanced Summon, Friend Summon y
  Tree of Knowledge.
- 37.61s: Tree of Knowledge. Hero Selection, moneda roja 49, heroes SSR/SR
  seleccionables, coste 5, Storage 1, refresh automatico despues de 5 dias.
- 37.61s: Tree of Knowledge muestra texto VIP14 o superior compra intentos +1.
- 51.47s: pantalla Hero. Coleccion 111/130, filtro All, boton Resonance.
- 51.47s-71.27s: heroes con rarezas UR, SSR, SR y R. Roles visibles:
  ATK, DEF, SUP.
- 98.99s: Handbook. Filtros Default y HP Boost, contador 12/127, cartas SSR
  Lv.300.

Sistemas nuevos confirmados:

- Ofertas/top up de skins.
- Adventure/campaña con Challenge Boss.
- Recompensas idle acumuladas con eficiencia por hora.
- Summon dividido en Common, Advanced, Friend y Tree of Knowledge.
- Advanced Summon con pity/progreso Grants SSR 70/800.
- Summon puede dar fragmentos de heroe, observado Kuro x80.
- Heroes tiene coleccion, rarezas, roles, fragmentos, finishing move y handbook.
- Finishing Move tiene pantalla propia, lista de remates y Finishing Move
  Resonance.
- Capturas nuevas de Finishing Move:
  `images/heroes/finishing-move/heroes-finishing-move-lineup.jpeg`,
  `images/heroes/finishing-move/heroes-finishing-move-resonance.jpeg`,
  `images/heroes/finishing-move/hero-grand-impact-detail.jpeg`,
  `images/heroes/finishing-move/hero-clap-detail.jpeg`.
- Grand Impact y Clap muestran detalles de remate, nivel 300/300, botones de
  Advance/Reshape/Upgrade y daño por porcentaje.
- Terminating Power es material de mejora de Finishing Move.
- Terminating Soul es material de Reshape de Finishing Move.
- Cage Shard junta 100 shards para componer el Finishing Move Cage.
- EXP Pass y oro suben niveles de heroes.
- Breakthrough Pass rompe limites de nivel en 20, 40, 60, 80, 100 y luego cada
  10 niveles.
- Nueva base de cards en `heroes.html`:
  - Filtros por nombre, rareza, rol, afinidad y estado de skills.
  - Afinidades visibles en capturas: Pirate, Captain, Legendary, No.1
    Swordsman, Four Emperors, Big Mom Band, Beasts Pirates, Marine,
    Marine Admirals, Marine Marshall, Marine Science Troop, Logia Fruit,
    Superman Fruit, Zoan Fruit, Artificial Fruit, Undercover, Wano Country,
    Fish Man, Strawhat Pirates, Sun Pirates, A.S.L, Buggy Pirates,
    Thriller Bark, Royal Deputy, Rebels, Germa, Skypiea Priest,
    Skypiea Residence, Baroque, Water 7, Worst Generation, Bliking Pirates,
    SHICHIBUKAI, Greed, Gentleman, Blackbeard Pirates, Whitebeard Pirates,
    Celestial Dragons, Donquixote, CP0, CP9, Okama, Impel Down y Royalty.
  - En la wiki, Superman Fruit se marca tambien como Paramecia para que el
    filtro sea mas facil de leer en español, pero se conserva el nombre del
    juego como etiqueta principal.
  - Big Mom, Rayleigh, Kaido y Cracker quedan como fichas completas iniciales
    con miniaturas y valores de habilidades.
  - Nuevas fichas completas agregadas desde capturas:
    - Luffy (Gear 2): SR ATK. Afinidades A.S.L, Superman Fruit, Paramecia,
      Strawhat Pirates, Worst Generation, Pirate y Captain. Jet - Pistol hace
      72% ATK a todos y aplica Heal Reduce 30% por 3 turnos; tiene pasivas de
      +35% DMG Reduction tras Jet Pistol, +100% Hit Rate con otro Strawhat
      Pirates y +25% Crit Rate / +50% Crit DMG si hay mas de 3 enemigos.
    - Bartolomeo: SSR ATK. Afinidades Pirate, Superman Fruit y Paramecia.
      Barrier Breakthrough hace 80% ATK a todos y baja Dodge Rate 5% por 2
      turnos; sus pasivas dan +40% Crit Rate, +30% Crit DMG, daño extra contra
      objetivos bajo 45% HP, escudo de 25% HP, hasta +20% DMG por benefit
      reduction y 100% de energia cuando cae bajo 45% HP.
    - Zoro: R ATK. Afinidades Strawhat Pirates, Pirate y No.1 Swordsman. Ghost
      Slash pega a 1 enemigo en 3 etapas por 168% ATK total; sus pasivas bajan
      Hit Rate 25% por 2 turnos tras Oni Giri y dan +50% Combo Rate / +21%
      Combo Damage.
    - Usopp: N ATK. Afinidades Strawhat Pirates y Pirate. Ultimate - Fire Bird
      Star hace 60% ATK a todos; Bravado tiene 12% de probabilidad de aplicar
      Terror por 1 turno tras la activa.
  - Recomendaciones de compra/equipamiento observadas en Hero Comment:
    - Jack: Dial azul, arma Iron y set Defend.
    - Smoothie: dial tipo concha, arma Paper y set Wrath.
    - Katakuri: dial rojo de espiral, arma Arashi y set Explode.
    - Akainu (New World): dial rojo de espiral, arma Arashi y set Explode.
    - Luffy (Gear 4): dial rojo de espiral, arma Arashi y set Explode.
    - Enel: dial rojo de espiral, arma Arashi y set Explode.
    - Zoro (New World): dial rojo de espiral, arma Arashi y set Explode.
    - Luffy (Gear 2): dial rojo de espiral, arma Arashi y set Explode.
    - Bartolomeo: dial rojo de espiral, arma Arashi y set Explode.
    - Zoro R: dial tipo concha, arma Gun y set Combo Slash.
    - Usopp: dial tipo concha, arma Paper y set Explode.
  - Katakuri y Akainu quedan como fichas iniciales desde comparativas,
    pendientes de capturas de skills.
- Skills observadas de Big Mom:
  - Raitei: activa de área. Hace daño igual al 80% del ATK de Big Mom a todos
    los enemigos. Si está en Calm, además hace 150% del ATK a 1 enemigo. Si
    está en Fury, aplica Serious Wound con 18% de daño por 2 turnos. Al terminar,
    Serious Wound causa daño extra según el daño total recibido durante esos 2
    turnos.
  - Eating Disorder: pasiva. Big Mom gana +40% Crit Rate y +30% Crit DMG
    durante toda la batalla. Si al inicio hay un aliado Big Mom Band, entra en
    Calm y gana +50% Break Rate. Si no, entra en Fury y gana +20% Crit Rate
    adicional.
  - Soul Pocus: pasiva. Big Mom hace +15% DMG mientras está en batalla. Si el
    objetivo está en Control, el bonus de daño sube a +35% DMG.
  - Soul Deterrence: pasiva ligada a Raitei. Raitei reduce el daño que causa el
    objetivo en 10% durante 2 turnos. Si el objetivo queda por debajo de 45% HP,
    aplica Terror por 2 turnos. Terror solo puede activarse 1 vez cada 6 turnos
    y tiene 50% de probabilidad de impedir que el objetivo se mueva.
  - Soul Tax: pasiva. Cada vez que muere un héroe en el campo, Big Mom gana +5%
    Crit DMG, hasta 5 acumulaciones. Máximo base: +25% Crit DMG. Con Awaken Red
    5-Star sube a +7% Crit DMG por muerte, máximo +35% Crit DMG.
- Skills observadas de Rayleigh:
  - Pluto: activa de área. Hace daño igual al 80% del ATK de Rayleigh a todos
    los enemigos. Además aumenta su Dodge Rate +3%, hasta 5 acumulaciones.
    Máximo visible: +15% Dodge Rate.
  - Haki Expert: pasiva. Rayleigh gana +40% Crit Rate y +30% Crit DMG mientras
    está en batalla. Cuando la energía está llena, tiene 50% de probabilidad de
    ganar Kenbunshoku; ese estado aumenta +25% el Crit Rate del siguiente
    ataque. También tiene 50% de probabilidad de ganar Busoshoku; ese estado
    aumenta +21% el siguiente daño. También tiene 50% de probabilidad de ganar
    Haoshoku; ese estado aumenta +21% el daño de la siguiente habilidad.
  - Legendary First Mate: pasiva. Al inicio del turno, si Rayleigh está en
    cualquier estado Haki, obtiene un escudo igual al 54% de su ATK.
  - Excessive Strike: pasiva. Cuando la energía está llena, la probabilidad de
    ganar estado Haki sube a 70%.
  - Eyes of Heart: pasiva. Mientras Rayleigh está en estado de escudo, aumenta
    su Crit DMG +25%.
- Skills observadas de Kaido:
  - Bolo Breath: activa de área. Hace daño igual al 80% del ATK de Kaido a todos
    los enemigos y aplica Healing Reduction de 20% durante 3 rondas. Healing
    Reduction reduce la curación recibida.
  - Strongest Creature: pasiva central. Kaido gana +28% Crit Rate y +21% Crit
    DMG durante la batalla. Al inicio reduce su propio HP en 50%. Después de
    morir, revive en la siguiente ronda con 64% HP. Se activa 1 vez por partida.
  - Kosanze Ragnaraku: pasiva posterior a la resurrección. Después de resucitar,
    Kaido gana +9% Crit DMG y +5% Hit Rate.
  - Kundali Dragon Swarm: pasiva posterior a la resurrección. Después de
    resucitar, el efecto de curación de sus habilidades activas aumenta a 100%
    durante 3 rondas.
  - Beasts: pasiva de acumulación. Cuando recibe un golpe crítico, Kaido acumula
    1 marca Beasts, hasta 3. Con marcas completas, el daño de la siguiente
    habilidad activa aumenta +20% y las marcas se consumen. Al revivir gana
    marcas completas inmediatamente.
- Skills observadas de Cracker:
  - Biscuit Assault: activa de área. Hace daño igual al 80% del ATK de Cracker a
    todos los enemigos y aplica Heal Reduce de 30% durante 3 turnos. Heal Reduce
    reduce la curación recibida.
  - Biscuit Hell: pasiva central. Cracker gana +40% Crit Rate y +30% Crit DMG.
    Al inicio obtiene 5 etapas de +10% DMG Increase y pierde 1 etapa al final de
    cada turno. Lectura práctica: empieza con hasta +50% DMG Increase.
  - Crush Biscuit: pasiva. El primer ataque común causa daño adicional igual al
    6% del HP del objetivo, con tope de 220% del ATK propio.
  - Hard Biscuit: pasiva. Al inicio de la batalla gana +15 SPD. Aplica Terror por
    2 turnos al objetivo con HP mayor a 80%, solo 1 vez por batalla. Terror tiene
    50% de probabilidad de impedir que el objetivo se mueva.
  - Pretzel: pasiva. Cada etapa de Biscuit Hell aumenta el Hit Rate de Cracker
    +6%; con 5 etapas puede iniciar con +30% Hit Rate.



Pendiente:

- Confirmar usos exactos de los recursos idle verde, azul y violeta.
- Confirmar si Tree of Knowledge usa una moneda exclusiva.
- Confirmar si Grants SSR 70/800 es pity garantizado o contador de progreso.
- Capturar Reward Preview, Wishlist, Friend Summon y reglas exactas de
  Resonance.

## Video fuente 3

Imagen/video: `images/videos/WhatsApp Video 2026-07-09 at 22.30.21.mp4`

Observado del archivo:

- Formato: MP4.
- Tamaño aproximado: 21.6 MB.
- Duracion extraida con OpenCV: 175.05s.
- FPS extraido con OpenCV: 24.23.
- Capturas seleccionadas del video: 8 en `images/videos/video3-frames-2s/`.

Lectura del video:

- 00.00s: Main City, pantalla principal.
- 09.91s: Arena Store. Moneda visible: 8200. Store Level: 3.
- 09.91s: Arena Store muestra tabs superiores: Altar Store, Arena Store,
  Senior Arena Store, Guild Shop, Showdown Store y otros parcialmente visibles.
- 09.91s: Arena Store refresca automaticamente despues de 05 Day(s).
- 09.91s: productos visibles: fragmentos UR x10, coste 24000, Storage 2/3,
  uno aparece Sold Out.
- 33.68s: Altar Hero Rebirth. Moneda violeta visible: 1437. Boton Rebirth,
  opcion Keep Star Level y coste 0 diamantes.
- 41.61s: Altar principal separa Hero, Gear, Weapon y Dial.
- 41.61s: Hero tiene Rebirth, Dissolve, Swap.
- 41.61s: Gear y Weapon tienen Rebirth, Dissolve, HP Boost.
- 41.61s: Dial tiene Rebirth y Dissolve.
- 49.53s: Weapon Dissolve. Moneda amarilla visible: 1088. Botones Fast
  Filter, Dissolve, Dissolve Preview. Armas Paper/Gun Lv1.
- 61.42s: Dial Fast Filter. Tipos visibles: Impact Dial, Flame Dials, Tone
  Dials, Breath Dials, Water Dial, Flash Dial. Filtros de color Green, Blue,
  Purple.
- 152.55s: detalle de heroe Big Mom. UR, ATK, Level 270/280, Power 143.5M,
  Qualification 608.
- 152.55s: stats Big Mom: ATK 1382221, HP 17553497, DEF 43821, SPD 403.
- 152.55s: pestañas de detalle: Info, Skill, Dial, Talent.
- 162.46s: skill pasiva Eating Disorder. Aumenta Crit Rate, Crit DMG,
  Break Rate y alterna estados Calm/Fury segun condicion Big Mom Band.
- 172.36s: skill pasiva Soul Tax. Cuando un heroe muere en el campo,
  aumenta Crit DMG de Big Mom, acumulando hasta 5 stacks. Con Awaken Red
  5-Star mejora de 5% a 7%.

Sistemas nuevos confirmados:

- Arena Store con nivel de tienda, stock, refresh, moneda e items de fragmentos.
- Altar como sistema de reciclaje/reinicio para Hero, Gear, Weapon y Dial.
- Dials tienen tipos y colores.
- Detalle de heroe muestra stats, qualification, relaciones, skills, dial y talent.
- Skills pueden tener niveles, requisitos de awaken y condiciones de estado.

Pendiente:

- Confirmar monedas exactas de Arena Store, Altar Hero, Weapon y Dial.
- Confirmar que recursos devuelve Rebirth/Dissolve por cada categoria.
- Capturar Altar Store y Senior Arena Store.
- Confirmar efectos de HP Boost en Gear/Weapon.
- Registrar todas las skills de Big Mom y sus niveles.

## Estrategia: duos y resumen de danos

Imagenes fuente:

- `images/strategy/resumen-danos.jpeg`
- `images/strategy/duo big mom y cracker.jpeg`
- `images/strategy/duo katakuri y akainu.jpeg`
- `images/strategy/duo rayleigh y kaido.jpeg`

Notas de lectura:

- Son ejemplos de pruebas y no valores finales. Cambian con items, diales,
  talentos, awaken, buffs, nivel, formacion y enemigo.
- La base de comparacion del resumen es basico normal = 100% para cada
  personaje.
- Big Mom destaca mucho frente al resto: basico critico 280,9% y habilidad
  critica potenciada 1236,0% en el resumen.
- Rayleigh queda como muy buena opcion de critico: 205,6% en basico critico y
  295,5% en habilidad critica potenciada.
- Katakuri y Akainu quedan casi empatados en productividad maxima confirmada:
  Katakuri 196,1% y Akainu 195,4%.
- Cracker tiene dano base alto y crecimiento mas estable, pero menor salto
  relativo en habilidad critica potenciada.
- Kaido mejora con buffs de forma estable, aunque escala menos que Rayleigh en
  criticos dentro de esta prueba.

Buenas opciones iniciales:

- Big Mom como carry explosivo de habilidad critica potenciada.
- Rayleigh como atacante critico fuerte y mas regular.
- Katakuri/Akainu como dupla para comparar dano por rafagas y multi-hit.
- Cracker/Kaido como piezas estables segun equipo, buffs y rol del combate.


## Social y VIP

Im?genes fuente:

- `images/social/friends-list.jpeg`
- `images/social/friends-recommend-search.jpeg`
- `images/social/friends-applications.jpeg`
- `images/social/friends-blacklist-empty.jpeg`
- `images/vip/premium-month-pass.jpeg`
- `images/vip/vip-1-perk.jpeg` a `images/vip/vip-19-perk.jpeg`

Lectura inicial:

- Friends muestra Friend Count 30/30.
- Acciones visibles: Attack Lineup y Fast Claim and Send.
- Pestañas visibles: Friends, Recommend, Applications y Blacklist.
- Applications permite aceptar o rechazar solicitudes.
- Blacklist puede estar vacía.
- VIP Perk fue capturado desde VIP1 hasta VIP19.
- Premium Month Pass, Month Breakthrough Pass y Month Summon Pass aparecen como
  pases mensuales separados.
- Los perks VIP aumentan principalmente Idling Yield, cantidad de paquetes,
  intentos de compra, refresh de Market e intentos extra en modos como Instance,
  Impel Down, Skypiea Race, Arena y Voyage Adventure.

Pendiente:

- Transcribir una tabla exacta VIP1-VIP19 con cada valor, idealmente desde
  capturas ampliadas o recortes por nivel.

