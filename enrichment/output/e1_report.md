# E1 — Reporte de cobertura del pre-seed heuristico

**Total ejercicios:** 1324

## Cobertura por campo

| Campo | Resueltos | Cobertura | Pendiente para E2 |
|---|---:|---:|---:|
| `start_position` | 1253 | 94.6% | 71 |
| `requires_balance` | 1137 | 85.9% | 187 |
| `overhead_position` | 169 | 12.8% | 1155 |
| `grip_required` | 1166 | 88.1% | 158 |
| `laterality` | 582 | 44.0% | 742 |
| `movement_pattern` | 971 | 73.3% | 353 |
| `axial_spinal_load` | 410 | 31.0% | 914 |
| `impact_level` | 34 | 2.6% | 1290 |
| `setup_complexity` | 1251 | 94.5% | 73 |

## Distribucion de `start_position`

| Valor | N |
|---|---:|
| standing | 562 |
| seated | 237 |
| supine | 95 |
| bench_supine | 79 |
| **(sin resolver)** | 71 |
| bench_incline | 59 |
| seated_machine | 57 |
| plank | 52 |
| hanging | 43 |
| prone | 29 |
| kneeling | 28 |
| bench_prone | 8 |
| quadruped | 3 |
| half_kneeling | 1 |

## Fuente de inferencia de `start_position`

| Fuente | N |
|---|---:|
| text | 814 |
| name+text | 286 |
| text(conflict) | 94 |
| (ninguna) | 71 |
| name | 47 |
| text(wide) | 6 |
| equipment | 6 |

## Distribucion de `movement_pattern`

| Valor | N |
|---|---:|
| isolation | 363 |
| **(sin resolver)** | 353 |
| horizontal_push | 156 |
| horizontal_pull | 93 |
| squat | 85 |
| core_flexion | 72 |
| vertical_pull | 51 |
| vertical_push | 34 |
| core_rotation | 31 |
| cardio_steady | 29 |
| hinge | 24 |
| lunge | 23 |
| core_antiextension | 8 |
| carry | 2 |

## Cola de trabajo para E2 (IA)

- Ejercicios con `start_position` sin resolver: **71**
- Ejercicios con confianza agregada < 0.75: **77**
- Campos de seguridad sin tocar por heuristica (100% pendiente): `joint_stress`, `contraindications`, `cautions`, `safe_for`, `spinal_flexion/extension/rotation`, `rom_demand`, `difficulty`
