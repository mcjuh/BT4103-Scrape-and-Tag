<!-- Source: https://research.thoughtworks.com/library/beyond-mae-measuring-forecast-reliability-tde | Title: Beyond MAE: Measuring forecast reliability with temporal dependence-aware error (TDE) | Thoughtworks AI Labs | Seed: https://www.thoughtworks.com/ (ThoughtWorks) -->

Research
# Beyond MAE: Measuring forecast reliability with temporal dependence-aware error (TDE)
By 
Aditi Gautam and
Alisha Chulani
Published: December 08, 2025 
Error metrics for time-series forecasting typically treat deviations as independent, ignoring whether errors occur as isolated points or in temporal bursts. This under specification limits their ability to capture operational risk in deployment-critical domains such as energy, transport, and weather forecasting. We introduce the Temporal Dependence-Aware Error (TDE), a streak-sensitive extension of mean absolute error (MAE) that penalizes temporally clustered errors more heavily. TDE is theoretically grounded, satisfying reduction, boundedness, and monotonicity properties, and admits smooth and asymmetric variants for differentiable optimization and cost-sensitive evaluation. We validate TDE through five experiments. Synthetic tests confirm its axiomatic properties and demonstrate that TDE distinguishes clustered from scattered errors with identical MAE. Benchmark evaluations show that TDE preserves broad leaderboard trends while surfacing differences in reliability, and event-window analysis highlights its sensitivity to holiday, rush-hour, and storm intervals where errors are most costly. Finally, we show that smooth and asymmetric variants maintain ranking fidelity while enabling adaptation to deployment-specific objectives.
**Find the full research paper here:[IEEE](https://ieeexplore.ieee.org/abstract/document/11402385/)**