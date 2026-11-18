# AI / Agentic AI Interview Revision

## LLM Fundamentals
**What is it?** A large language model predicts likely next tokens from context. **Key idea:** It is probabilistic, so outputs need validation. **Interview answer:** "An LLM generates text from context and learned patterns; it does not inherently retrieve facts or execute reliable reasoning." **Example:** Draft support responses from a policy document. **Use:** Generation and transformation. **Points:** Prompt, context, decoding, hallucination. **Follow-ups:** RAG vs fine-tuning.

## Tokens & Context Window
**What is it?** Tokens are model text units; context window is the maximum input and output capacity. **Key idea:** More context increases cost and can reduce retrieval precision. **Interview answer:** "Chunked text and retrieved evidence must fit the context limit and leave room for the response." **Example:** Summarize a long contract in chunks. **Use:** Prompt budgeting. **Points:** Tokenization, limits, truncation. **Follow-ups:** Long context costs.

## Prompt Engineering
**What is it?** Prompt engineering designs instructions and examples for reliable model behavior. **Key idea:** Specify role, task, constraints, format, and evidence. **Interview answer:** "I give the model a schema and explicit unknown handling instead of asking for a vague answer." **Example:** Extract invoice fields into JSON. **Use:** Controllable output. **Points:** Zero/few-shot, chain of thought alternatives. **Follow-ups:** Prompt injection.

## Structured Outputs
**What is it?** Structured output forces a model to return typed JSON or another schema. **Key idea:** Schemas reduce downstream parsing failures. **Interview answer:** "I validate model JSON with Pydantic or JSON Schema and retry or fall back on invalid output." **Example:** Return a support ticket category and confidence. **Use:** Tool and API integration. **Points:** Schema constraints, validation. **Follow-ups:** Function calling.

## Embeddings
**What is it?** Embeddings are vectors that encode semantic similarity. **Key idea:** Similar meanings usually have closer vectors. **Interview answer:** "I embed documents and questions into the same model space, then retrieve nearby documents." **Example:** Find policies similar to a user question. **Use:** Search and clustering. **Points:** Model choice, dimension, normalization. **Follow-ups:** Embedding drift.

## Vector Databases
**What is it?** Vector databases store and search embeddings efficiently. **Key idea:** Approximate nearest-neighbor search trades speed for recall. **Interview answer:** "A vector database retrieves the closest document chunks for a RAG pipeline." **Example:** pgvector or Pinecone-like search. **Use:** Semantic retrieval. **Points:** ANN, metadata filter, index. **Follow-ups:** HNSW, recall.

## RAG Pipelines
**What is it?** RAG retrieves relevant evidence and provides it to an LLM for grounded generation. **Key idea:** Retrieval quality determines answer quality. **Interview answer:** "I chunk documents, embed them, retrieve relevant passages, rerank them, and ask the model to answer with citations." **Example:** Internal policy assistant. **Use:** Private or changing knowledge. **Points:** Chunking, retrieval, reranking, grounding. **Follow-ups:** RAG vs fine-tuning.

## Chunking Strategies
**What is it?** Chunking splits source documents into retrievable units. **Key idea:** Preserve semantic boundaries and overlap. **Interview answer:** "I use heading-aware or recursive chunks and add overlap to avoid cutting key context." **Example:** Split a handbook by section. **Use:** RAG ingestion. **Points:** Size, overlap, metadata. **Follow-ups:** Chunk too small vs large.

## Reranking
**What is it?** Reranking reorders retrieved candidates using a more accurate relevance model. **Key idea:** It improves precision after broad retrieval. **Interview answer:** "Vector search retrieves 50 candidates; a cross-encoder reranker selects the top five." **Example:** Legal document search. **Use:** High-precision RAG. **Points:** Recall vs precision, latency. **Follow-ups:** Cost trade-off.

## Tool Calling
**What is it?** Tool calling lets a model request a validated external function. **Key idea:** The model proposes; deterministic code executes. **Interview answer:** "For an account action, the model emits a typed tool request, and the application checks authorization before execution." **Example:** Calendar booking. **Use:** AI with external effects. **Points:** Schemas, permissions, confirmation. **Follow-ups:** Tool loop limits.

## MCP Protocol
**What is it?** Model Context Protocol standardizes connections between AI clients and tools or resources. **Key idea:** Expose tools and context through a consistent protocol. **Interview answer:** "A coding assistant uses MCP to discover approved file, database, or ticket tools." **Example:** MCP server for an issue tracker. **Use:** Interoperable agent tooling. **Points:** Discovery, transport, authorization. **Follow-ups:** MCP vs direct API.

## ReAct Agent Loop
**What is it?** ReAct alternates reasoning traces with tool actions. **Key idea:** Observe tool output before choosing the next action. **Interview answer:** "The agent thinks, calls a tool, observes its result, and repeats until it can answer." **Example:** Diagnose a deployment from logs. **Use:** Dynamic multi-step work. **Points:** Loop limit, evidence, action validation. **Follow-ups:** Hallucinated tools.

## Planning & Reflection
**What is it?** Planning decomposes a goal; reflection evaluates progress and errors. **Key idea:** Reflection improves quality only with feedback. **Interview answer:** "The agent creates a task plan and revises it after a failed tool call." **Example:** Research and summarize a topic. **Use:** Complex workflows. **Points:** State, critique, retry limits. **Follow-ups:** Infinite loops.

## Agent Memory
**What is it?** Agent memory stores context across turns or tasks. **Key idea:** Separate short-term, long-term, and tool state. **Interview answer:** "I keep current state in context, retrieve durable memory by relevance, and require confirmation before updating sensitive memory." **Example:** Prefer a user's language and project conventions. **Use:** Personal assistants. **Points:** Expiry, privacy, contradiction. **Follow-ups:** Memory poisoning.

## Multi-Agent Systems
**What is it?** Multiple specialized agents collaborate on work. **Key idea:** Specialization helps but coordination adds failure modes. **Interview answer:** "A researcher, critic, and executor agents can divide tasks, but shared state and handoffs must be explicit." **Example:** Code review pipeline. **Use:** Complex decomposable work. **Points:** Roles, messages, consensus. **Follow-ups:** When not to use multi-agent.

## Agent Orchestration
**What is it?** Orchestration coordinates agent steps, tools, retries, and exits. **Key idea:** Control flow should remain explicit and observable. **Interview answer:** "A workflow engine routes tasks and pauses for human approval instead of letting agents run indefinitely." **Example:** Incident triage. **Use:** Production agents. **Points:** Graph, retries, budgets. **Follow-ups:** Agent framework lock-in.

## Guardrails
**What is it?** Guardrails enforce safety and business constraints around model behavior. **Key idea:** They are policy controls, not prompts alone. **Interview answer:** "I validate input, constrain tools, redact secrets, and confirm high-impact actions." **Example:** Reject transfer instructions outside limits. **Use:** Production AI. **Points:** Input/output filters, policy. **Follow-ups:** Guardrail bypass.

## Evals
**What is it?** Evals measure AI quality on representative tasks. **Key idea:** Combine objective, reference, and human judgments. **Interview answer:** "I evaluate retrieval recall, answer correctness, refusal behavior, and tool success on a versioned test set." **Example:** Policy assistant benchmark. **Use:** Model and prompt changes. **Points:** Regression, drift, cost. **Follow-ups:** Evals vs production monitoring.

## Observability & Tracing
**What is it?** AI tracing records prompts, retrieval, tool calls, latency, cost, and outcomes. **Key idea:** Protect sensitive prompt data and correlate traces. **Interview answer:** "A trace links retrieval candidates, model call, tool call, and final response." **Example:** Debug a wrong support answer. **Use:** Production AI operations. **Points:** Trace IDs, sampling, redaction. **Follow-ups:** PII.

## Fine-Tuning with LoRA
**What is it?** LoRA adds small trainable matrices instead of updating every model weight. **Key idea:** It adapts behavior with less compute and storage. **Interview answer:** "LoRA can teach a domain style or classification behavior, but RAG is usually better for changing facts." **Example:** Support-ticket tone adaptation. **Use:** Stable learned behavior. **Points:** Rank, data quality, base model, overfit. **Follow-ups:** LoRA vs full fine-tuning.
