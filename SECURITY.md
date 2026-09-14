# 安全策略

## 受支持版本

我们优先为本仓库 **最新 PyPI 发布版本** 与 **`main` 分支** 提供安全修复。更早的 tag 或提交可能不会收到补丁。

## 报告漏洞

请通过本仓库的 [GitHub Security Advisories](https://github.com/zendev-lab/dns-manager/security/advisories/new) **私下** 报告安全问题。请勿公开开 Issue。

请尽量提供：

- 问题及其影响的简要说明（例如凭证泄露、未授权 DNS 变更、依赖漏洞的可利用路径）
- 复现步骤，或在安全前提下可用的概念验证（PoC）
- 已知受影响版本（PyPI 版本、git tag 或 revision）

我们会在可行时尽快确认收到，并在合适情况下与你协调披露时间。

## 依赖安全更新

本仓库通过 Renovate 自动提出依赖更新；上游发布安全修复后，通常会经该流程合入。
