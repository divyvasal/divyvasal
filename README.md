### Hi, I'm Divy 👋

Building fast LLM inference at [Coral Bricks](https://coralbricks.ai). I fix things in the engines we run in production.

<!-- contributions:start -->
#### Open-source contributions · 6 merged · 13 open · 8 reported

**vLLM** <sub>· 2 merged · 0 open · 1 reported</sub>  
🟣 [#58457](https://github.com/vllm-project/vllm/pull/58457) Catch a block size a backend rejects, at startup  
🟣 [#49845](https://github.com/vllm-project/vllm/pull/49845) Start mixed-attention models without `--block-size`  
🐞 [#49844](https://github.com/vllm-project/vllm/issues/49844) Garbage output with PP=2 on GLM-MoE-DSA when torch.compile and CUDA graphs combine  

**SGLang** <sub>· 1 merged · 4 open · 4 reported</sub>  
🟣 [#38932](https://github.com/sgl-project/sglang/pull/38932) Fix NVFP4 crash with adaptive speculative decoding  
🟢 [#42812](https://github.com/sgl-project/sglang/pull/42812) Fix a DeepSeek-V4 hang with HiCache and DSPARK  
🟢 [#41379](https://github.com/sgl-project/sglang/pull/41379) Test image tokens in usage on the chat path  
🟢 [#41324](https://github.com/sgl-project/sglang/pull/41324) Stop one logprobs stream from stalling the server  
🟢 [#39240](https://github.com/sgl-project/sglang/pull/39240) Fix Gemma 4 tool calls with mangled arguments  
🐞 [#42548](https://github.com/sgl-project/sglang/issues/42548) DeepSeek-V4 HiCache: the SWA host pool is too small, so idle prefixes miss the host tier  
🐞 [#42465](https://github.com/sgl-project/sglang/issues/42465) DeepSeek-V4 + HiCache: TP ranks deadlock under concurrent long prefills  
✅ [#38795](https://github.com/sgl-project/sglang/issues/38795) NVFP4 + adaptive speculative decoding fails CUDA-graph capture  
✅ [#32459](https://github.com/sgl-project/sglang/issues/32459) EAGLE speculative decoding silently collapses multi-turn prefix reuse  

**LMCache** <sub>· 3 merged · 8 open · 2 reported</sub>  
🟣 [#4830](https://github.com/LMCache/LMCache/pull/4830) Fix silent KV cache corruption  
🟣 [#4079](https://github.com/LMCache/LMCache/pull/4079) Share KV copy code across transfer modes  
🟣 [#4015](https://github.com/LMCache/LMCache/pull/4015) Free a dead client's pinned GPU memory  
🟢 [#4944](https://github.com/LMCache/LMCache/pull/4944) Fix flaky port collisions in MQ tests  
🟢 [#4410](https://github.com/LMCache/LMCache/pull/4410) Hybrid-attention models in engine-driven mode  
🟢 [#4072](https://github.com/LMCache/LMCache/pull/4072) Survive a cache server restart without crashing vLLM  
🟢 [#4068](https://github.com/LMCache/LMCache/pull/4068) Release locks on skipped cache writes  
🟢 [#3992](https://github.com/LMCache/LMCache/pull/3992) Correct the hybrid-models docs  
🟢 [#3932](https://github.com/LMCache/LMCache/pull/3932) Keep serving when the S3 tier hits its cap  
🟢 [#3909](https://github.com/LMCache/LMCache/pull/3909) Rebuild S3 tier state after a restart  
🟢 [#3892](https://github.com/LMCache/LMCache/pull/3892) One S3 bucket per tenant  
🐞 [#4071](https://github.com/LMCache/LMCache/issues/4071) Design proposal: hybrid-attention (multi-group KV) support for engine-driven transport  
✅ [#4014](https://github.com/LMCache/LMCache/issues/4014) The server keeps a dead vLLM client's KV pool memory until it restarts  

**FlashInfer** <sub>· 0 merged · 1 open · 1 reported</sub>  
🟢 [#4885](https://github.com/flashinfer-ai/flashinfer/pull/4885) Stabilize JIT cached ops across environments  
🐞 [#4884](https://github.com/flashinfer-ai/flashinfer/issues/4884) JIT cached ops rebuild needlessly (PATH-dependent CUDA home, mtime staleness)  

<sub>🟣 merged · 🟢 open · ⚪ draft · 🐞 issue reported · ✅ issue resolved · updated automatically every day</sub>
<!-- contributions:end -->
