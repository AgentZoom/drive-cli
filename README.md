# Drive CLI

`drive-cli` 是给 Agent 和自动化脚本使用的远程调用工具。它只调用后端 API，不负责启动网站前端，也不负责启动网站后端。

这个仓库刻意不包含任何网站运维职责：

- 不提供前端启动命令
- 不提供后端启动命令
- 不依赖前端是否在线
- 只要后端 API 可访问，CLI 就可以工作

## 安装

```bash
cd /Users/huangsy16/huangshiyu/Task/repos/AgentZoom/drive-cli
python -m pip install -e .
```

安装后可执行命令：

```bash
drive-cli --help
```

## 配置

默认服务器地址是：`http://drive.mm-lab.cn`

常见环境变量：

```bash
export DRIVE_BOARD_SERVER="http://127.0.0.1:8361"
export DRIVE_BOARD_TOKEN="your-agent-token"
export DRIVE_BOARD_FORMAT="json"
```

## 文档

完整命令说明见 [docs/cli-guide.md](docs/cli-guide.md)。