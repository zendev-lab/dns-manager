# Agent standing orders

面向在本仓库工作的编码代理的仓库级约定。产品说明与用法见 [`README.md`](./README.md)。

## 工作方式

- 优先在**独立 git worktree** 中修改，避免干扰主工作区未提交内容。
- 保持改动最小；不要发明与本工具无关的流程或功能。
- 行为变更时，同步更新相关文档（如 `README.md`）与验证说明。
- 不提交密钥、凭证或 `.env` 文件。

## 校验

使用仓库 `justfile` 入口，并如实报告实际执行过的命令：

- `just format` — 格式化
- `just check` — 静态检查（ruff / ty）
- `just test` — 测试与覆盖率

不要声称未运行过的检查已通过。

## 安全

安全问题请**私下**按 [`SECURITY.md`](./SECURITY.md)（GitHub Security Advisories）报告，勿开公开 Issue。

## Pull requests

- 变更尽量聚焦单一主题。
- PR 中说明改了什么、验证了什么、以及未验证的部分。
