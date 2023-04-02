# Notas Musicais

---

## Objetivos

Ajudar pessoas estudante de música a estudar teoria musical

- Ajudar no entendimento de escalas musicais

- Formação de acordes

- Ajudar no entendimento de campos harmônicos

- Ajudar com progressões harmônicas

---

## Como?

Eu gostaria de fazer uma aplicação de terminal (CLI) Que perguntada uma escala ou um campo harmônico ele exiba uma tabela com um progressão sugerida randomicamente!

---

## Notas

Notas: Dó - Ré - Mi - Fá - Sol - Lá - Si

Notas e acidentes: Dó - Dó# - Ré - Ré# - Mi - Fá - Fá# - Sol - Sol# - Lá - Lá# - Si

---

## Cifras

Notas e acidentes: C - C# - D - D# - E - F - F# - G - G# - A - A# - B

| Nome da nota | Naturais | Sustenidos (♯) | Bemóis (♭) |
| ------------ | -------- | -------------- | ---------- |
| Dó           | C        | C♯             | C♭         |
| Ré           | D        | D♯             | D♭         |
| Mi           | E        | E♯             | E♭         |
| Fá           | F        | F♯             | F♭         |
| Sol          | G        | G♯             | G♭         |
| Lá           | A        | A♯             | A♭         |
| Si           | B        | B♯             | B♭         |

---

## Escalas

Graus: I - II - II - IV - V - VI - VII

### Escala maior

Intervalos: T - T - ST - T - T - T - ST

| I   | II  | III | IV  | V   | VI  | VII |
| --- | --- | --- | --- | --- | --- | --- |
| T   | T   | ST  | T   | T   | T   | ST  |
| C   | D   | E   | F   | G   | A   | B   |
| C#  | D#  | F   | F#  | G#  | A#  | C   |

---

## Acordes

Triade maior: I - III - V

Triade Menor: I - III♭ - V

Triade diminuto: I - III♭ - V♭



### Campo harmônico

| I   | ii  | iii | IV  | V   | vi  | VII° |
| --- | --- | --- | --- | --- | --- | ---- |
| T   | T   | ST  | T   | T   | T   | ST   |
| C   | Dm  | Em  | F   | G   | Am  | B°   |

---

## Progressões harmônicas

I - IV - V



---

---

## Exemplo de uso!

```bash
notas-musicais c maior
```

Aplicação deve responder:

| I   | II  | III | IV  | V   | VI  | VII |
| --- | --- | --- | --- | --- | --- | --- |
| C   | D   | E   | F   | G   | A   | B   |

```bash
notas-musicais c maior --acordes | --campo | --harmonico | --chords
```

| I   | ii  | iii | IV  | V   | vi  | vii° |
| --- | --- | --- | --- | --- | --- | ---- |
| C   | Dm  | Em  | F   | G   | Am  | Bm°  |



Por exemplo, o campo progressões escala maior:

```bash
notas-musicais c maior --acordes --prog
```

E aplicação deve retornar:

```
| I   | ii  | iii | IV  | V   | vi  | vii° |
| --- | --- | --- | --- | --- | --- | ---- |
| C   | Dm  | Em  | F   | G   | Am  | Bm°  |

Tente: I - V - IV
```