# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeFinder 1.0  

---

## 2. Intended Use  

This recommender suggests songs that fit a user's genre, mood, energy, and acoustic preference. It is designed for learning and experimentation, not for production use. It assumes users can describe their music taste with a few simple labels.  

---

## 3. How the Model Works  

The model looks at each song and compares it to what the user likes. It gives points for matching genre and mood, and it adds a bigger bonus for energy that is close to the user's target. It also gives a small bonus when the acoustic feel matches the user's preference. The songs are then ranked by total score.  

---

## 4. Data  

The model uses a small CSV catalog of songs with features like genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is limited in size and mostly covers common categories. It does not include every genre or all possible mood labels.  

---

## 5. Strengths  

The system does well for clear profiles like upbeat pop and calm lofi. It captures energy differences and can separate intense rock from mellow songs. The top results often match what you would expect from the stated preferences.  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

During experimentation, I found that the scoring logic can become overly sensitive to a single feature when weights are changed. For example, doubling the energy importance caused songs with the right energy to rise above better genre or mood matches. This suggests the system may underweight nuanced taste signals and overfit to one strong preference. The current dataset also seems biased toward certain genres, so the recommendations can drift if one feature is emphasized too much. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested four distinct user profiles: `High-Energy Pop`, `Chill Lofi`, `Deep Intense Rock`, and an `Adversarial Edge Case` with conflicting preferences. I looked for whether the top recommendations matched the intended genre, mood, energy level, and acoustic preference for each profile. It was surprising how much the rankings shifted when I doubled the energy weight; energy alignment began to dominate the rankings even when genre was still relevant. I also checked how a mood mismatch affected the results, especially for the adversarial profile, and found that songs with the right energy could still outrank genre-matched tracks. The simple test of comparing outputs across these profiles helped confirm that the system behaves differently when different preferences are emphasized.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

I would add more genres, moods, and acoustic options so the model can cover more users. I would make the scoring rules easier to tune and more balanced. I would also add more song features like popularity or lyrics to improve ranking.  

---

## 9. Personal Reflection  

The biggest learning moment was seeing how one small weight change can change the whole ranking. I learned that a simple algorithm can still feel like a real recommendation when the features are chosen well. Using AI tools helped me iterate faster and keep the code focused on the scoring logic. I was surprised that clear user preferences and a few song features can produce outputs that feel valid. Next, I would try adding more features, balancing the weights better, and testing more diverse taste profiles.  
