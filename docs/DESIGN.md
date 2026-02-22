# ADR-022: CI Pipeline Architecture
**Decision:** 4-stage pipeline: Install -> Build -> Test -> Deploy
**Key Rule:** Deploy ONLY runs if all previous stages succeed.
