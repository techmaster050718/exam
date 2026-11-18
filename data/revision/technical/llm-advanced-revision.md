# AI / LLM Advanced Revision

## LangGraph
**What is it?** LangGraph models agent and workflow state as a graph. **Interview answer:** "Nodes perform work and edges route based on state, making retries and human approval explicit." **Example:** Research then reviewer workflow. **Use:** State-based agents. **Points:** State, checkpoint, cycles. **Follow-ups:** Graph vs autonomous loop.

## RAG Evaluation
**What is it?** RAG evaluation measures retrieval and generation quality separately. **Interview answer:** "I test whether the needed document was retrieved, whether the context is used, and whether the answer is factual." **Example:** Policy QA test set. **Use:** RAG improvement. **Points:** Recall, relevance, faithfulness. **Follow-ups:** Offline vs online.

## RAGAS
**What is it?** RAGAS is a framework of metrics for RAG retrieval and answer quality. **Interview answer:** "I use it as one signal, but supplement with domain rubric and human review." **Example:** Reference-free answer scoring. **Use:** Automated regression. **Points:** Faithfulness, relevancy, recall. **Follow-ups:** Metric bias.

## Semantic Caching
**What is it?** Semantic caching serves similar prior requests instead of exact-string matches. **Interview answer:** "I embed queries, search a cache threshold, and validate tenant and freshness." **Example:** Repeated policy questions. **Use:** Latency and cost. **Points:** Threshold, privacy, invalidation. **Follow-ups:** False cache hits.

## Hybrid Search
**What is it?** Hybrid search combines lexical and semantic retrieval. **Interview answer:** "I merge keyword BM25 matches with vector matches and rerank." **Example:** Find a policy by exact ID and concept. **Use:** Diverse queries. **Points:** Fusion, weighting. **Follow-ups:** Reciprocal rank fusion.

## BM25
**What is it?** BM25 ranks documents by term frequency and inverse document frequency. **Interview answer:** "It is strong for exact keywords and handles length and repetition." **Example:** Search by error code. **Use:** Lexical retrieval. **Points:** TF-IDF, stop terms. **Follow-ups:** BM25 vs embeddings.

## Vector Search
**What is it?** Vector search returns nearby embeddings by similarity. **Interview answer:** "I use metadata filters and ANN indexes, then evaluate recall." **Example:** Similar ticket search. **Use:** Semantic similarity. **Points:** Cosine, dot product, HNSW. **Follow-ups:** pgvector.

## LLM Cost Optimization
**What is it?** Cost optimization reduces model, token, retrieval, and tool expense. **Interview answer:** "I route simple tasks to cheaper models, cache, shorten context, and set token limits." **Example:** Classify with a small model. **Use:** Production AI budgets. **Points:** Per-call cost, cache. **Follow-ups:** Quality-cost trade.

## LLM Latency Optimization
**What is it?** Latency optimization reduces first-token and end-to-end delay. **Interview answer:** "I stream output, use smaller models, parallelize retrieval, and trim context." **Example:** Chat assistant. **Use:** Interactive products. **Points:** TTFT, throughput. **Follow-ups:** Batch inference.

## Streaming Responses
**What is it?** Streaming sends generated tokens as they are produced. **Interview answer:** "SSE or WebSockets improves perceived latency, while the client handles partial output and cancellation." **Example:** LLM answer and report generation. **Use:** Interactive AI. **Points:** Backpressure, partial JSON. **Follow-ups:** SSE vs WebSocket.
