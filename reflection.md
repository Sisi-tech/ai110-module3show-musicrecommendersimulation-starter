# Reflection on Recommendation Differences

- High-Energy Pop vs Chill Lofi: The high-energy profile prefers fast, upbeat songs like `Sunrise City`, while Chill Lofi shifts toward low-energy, relaxed tracks such as `Symphony of Dreams`. This makes sense because the former is testing energy and pop mood, while the latter is testing calm atmosphere and acoustic feel.

- High-Energy Pop vs Deep Intense Rock: Both profiles value high energy, but the rock profile also expects an intense mood and a rock genre. As a result, `Storm Runner` leads rock while `Sunrise City` leads pop, showing that genre and mood still guide the top pick even when energy is strong.

- High-Energy Pop vs Adversarial Edge Case: The adversarial profile has a pop genre preference but a sad mood and acoustic lean. The difference shows how mood and acoustic preference can pull the top choice away from the pure pop/happy recommendation, and it highlights the system's sensitivity to conflicting signals.

- Chill Lofi vs Deep Intense Rock: These profiles are nearly opposite in energy and mood. Chill Lofi favored calm, soft acoustic tracks, while Deep Intense Rock favored loud, driving songs. That contrast confirms the model is respecting the energy target and the specific mood labels.

- Chill Lofi vs Adversarial Edge Case: Both can prefer lower-energy or more emotional tracks, but the adversarial profile still has a pop genre bias and acoustic preference. The comparison shows that genre plus mood can shift the ranking even when both profiles are not high-energy.

- Deep Intense Rock vs Adversarial Edge Case: Deep Intense Rock is clearly oriented around aggressive rock energy, while the adversarial case is more about matching sad mood and acoustic style. The top results differ accordingly, which is a good sign that the recommender is reacting to the distinct user tastes.
