# Drive CLI

`drive-cli` 是一个面向客户和自动化脚本的命令行工具，用于访问兼容的 Drive 服务。

它只提供命令行访问能力，不包含部署、站点启动或运维相关逻辑。

## 安装

```bash
python -m pip install .
```

安装后可执行：

```bash
drive-cli --help
```

## 配置

默认服务地址是：`https://drive.mm-lab.cn`

常见环境变量：

```bash
export DRIVE_CLI_SERVER="https://drive.mm-lab.cn"
export DRIVE_CLI_TOKEN="your-access-token"
export DRIVE_CLI_FORMAT="json"
```

也可以在命令行里直接传入：

```bash
drive-cli --server https://drive.mm-lab.cn --token your-access-token --format json whoami
```

## 安全建议

- 使用专用的访问令牌，不要与其他系统复用。
- 不要把令牌写进仓库、脚本示例或截图。
- 优先通过环境变量或你的密钥管理系统注入令牌。
- 如果令牌疑似泄漏，立即轮换并废弃旧令牌。

## 文档

完整命令说明见 [docs/cli-guide.md](docs/cli-guide.md)。
