# Artificial Intelligence, Machine Learning & Big Data Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. MACHINE LEARNING PARADIGMS

| Paradigm | Description | Feedback / Signal | Typical Algorithms |
| :--- | :--- | :--- | :--- |
| **Supervised** | Model trains on labeled input-output pairs $(X, y)$ | Direct target error | Linear Regression, Logistic Regression, Decision Trees, SVM |
| **Unsupervised** | Discovers hidden patterns in unlabeled data $X$ | No external labels | K-Means, Hierarchical Clustering, PCA, Autoencoders |
| **Reinforcement** | Agent interacts with environment to maximize cumulative reward | Reward / Penalty signal | Q-Learning, Policy Gradients, SARSA |

---

## 2. MODEL EVALUATION & CONFUSION MATRIX

```text
                    Actual Positive          Actual Negative
Predicted Positive   True Positive (TP)       False Positive (FP) [Type I Error]
Predicted Negative   False Negative (FN) [Type II] True Negative (TN)
```

### Key Metrics Formulas:
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
$$\text{Precision} = \frac{TP}{TP + FP} \quad (\text{Quality of positive predictions})$$
$$\text{Recall (Sensitivity)} = \frac{TP}{TP + FN} \quad (\text{Ability to find all positives})$$
$$F_1\text{-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}$$

---

## 3. BIAS-VARIANCE TRADEOFF & REGULARIZATION
* **High Bias (Underfitting):** Model is too simplistic; misses key trends. High error on both training and test data.
* **High Variance (Overfitting):** Model memorizes training noise; poor generalization on unseen data.
* **Regularization Techniques:**
  * **L1 Regularization (Lasso):** Adds penalty $\lambda \sum |w_i|$. Induces **sparsity** (sets non-informative weights to 0 for feature selection).
  * **L2 Regularization (Ridge):** Adds penalty $\lambda \sum w_i^2$. Shrinks weights close to zero; preserves all features.
  * **Dropout:** Randomly deactivates neurons during training in deep neural networks.

---

## 4. DEEP LEARNING ACTIVATION FUNCTIONS
* **Sigmoid:** $\sigma(x) = \frac{1}{1 + e^{-x}}$, outputs in range $(0, 1)$. Vanishing gradient problem for extreme values.
* **Tanh:** $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$, outputs in range $(-1, 1)$, zero-centered.
* **ReLU (Rectified Linear Unit):** $f(x) = \max(0, x)$. Computationally trivial; prevents vanishing gradient for positive activations. Can suffer from "Dying ReLU".
* **Softmax:** Converts a vector of $K$ real values into a categorical probability distribution summing to 1.

---

## 5. APACHE HADOOP & BIG DATA ARCHITECTURE
* **HDFS (Storage):** Master-Slave Architecture.
  * **NameNode (Master):** Stores filesystem namespace directory tree and block metadata in RAM.
  * **DataNode (Slave):** Stores physical data blocks on local disks (default block size: 128 MB, default replication: 3).
* **MapReduce (Compute):** Splits computation into Map phase (key-value pairs) and Reduce phase (aggregation).
* **Apache Spark:** In-memory distributed computation framework using Resilient Distributed Datasets (RDDs); up to 100x faster than MapReduce.
