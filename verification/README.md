# Verification

From the repository root on Python 3.10 or later, run:

```bash
python verification/check_receiver.py
```

The script uses the standard library and checks port ratios and recovered coherence, the optimal weighted arrival-time baseline by exhaustive cyclic partitions, matching primal and dual chord examples, and finite sampling of the paired-quantile span bound. It prints one pass line for each check. These numerical exercises complement the analytical arguments in [the scientific account](../science/README.md). They do not simulate a physical optical device.

For the governing assumptions and proof dependencies, start with [Model and resources](../science/model.md) and follow the theorem, receiver, robustness and overlapping-window links in [the scientific route](../science/README.md).
