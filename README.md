# 0-LA RAG Test Repository

This repository is used to test Git synchronization and RAG retrieval in 0-LA.

## Test Information

The repository contains small documents designed to verify that synchronization correctly detects, imports, chunks, and indexes files.

The main test identifier is **RAG-TEST-2026**.

The expected test workflow is:

1. Synchronize the Git repository.
2. Review the detected file changes.
3. Activate the new repository version.
4. Generate document chunks and embeddings.
5. Ask questions about the synchronized documents through RAG.

A successful RAG test should return information directly from the repository files instead of the default "I cannot answer your query" response.
