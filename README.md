# MBTI-style preference explorer

This project started as a small personality-test prototype and is now a
transparent Python CLI demonstration. It shows how to model questionnaire
items as data, separate classification from user input, validate inputs, and
test deterministic rules.

It is deliberately described as an MBTI-style explorer rather than a
psychological assessment. The result is illustrative and should not be used
for diagnosis or important decisions.

## Run it

```bash
python mbti_explorer.py --answers A,B,A,B
python mbti_explorer.py
python -m pytest -q
```
