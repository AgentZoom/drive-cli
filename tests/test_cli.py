from __future__ import annotations

import json

import httpx
from typer.testing import CliRunner

from drive_cli import cli as cli_module


runner = CliRunner()


def test_default_server_uses_generic_local_endpoint():
    assert cli_module.DEFAULT_SERVER == "http://drive.mm-lab.cn"


def test_workspaces_add_member_requires_prefixed_actor_id(monkeypatch):
    def fail_request(method: str, url: str, **kwargs):
        raise AssertionError("request should not be called")

    monkeypatch.setattr(cli_module, "request", fail_request)

    result = runner.invoke(
        cli_module.app,
        ["workspaces", "add-member", "team-space", "--actor", "sample_agent_2", "--permission", "read"],
    )

    assert result.exit_code == 1
    assert "actor_id must include prefix" in result.output


def test_workspaces_add_member_rejects_invalid_permission_locally(monkeypatch):
    def fail_request(method: str, url: str, **kwargs):
        raise AssertionError("request should not be called")

    monkeypatch.setattr(cli_module, "request", fail_request)

    result = runner.invoke(
        cli_module.app,
        ["workspaces", "add-member", "team-space", "--actor", "agent:sample-agent", "--permission", "admin"],
    )

    assert result.exit_code == 1
    assert "permission must be one of: owner, read, write" in result.output


def test_shares_add_rejects_invalid_permission_locally(monkeypatch):
    def fail_request(method: str, url: str, **kwargs):
        raise AssertionError("request should not be called")

    monkeypatch.setattr(cli_module, "request", fail_request)

    result = runner.invoke(
        cli_module.app,
        ["shares", "add", "sample-space", "reports", "--actor", "agent:sample-agent", "--permission", "owner"],
    )

    assert result.exit_code == 1
    assert "permission must be one of: read, write" in result.output


def test_response_error_detail_formats_pydantic_error_lists():
    response = httpx.Response(
        422,
        headers={"content-type": "application/json"},
        json={
            "detail": [
                {"loc": ["body", "permission"], "msg": "Input should be 'read' or 'write'"},
                {"loc": ["body", "actor_id"], "msg": "Field required"},
            ]
        },
    )

    detail = cli_module.response_error_detail(response)

    assert detail == (
        "permission: Input should be 'read' or 'write'; actor_id: Field required"
    )


def test_response_error_detail_formats_object_payloads():
    response = httpx.Response(
        400,
        headers={"content-type": "application/json"},
        json={"detail": {"error": "bad request", "field": "path"}},
    )

    detail = cli_module.response_error_detail(response)

    assert detail == json.dumps({"error": "bad request", "field": "path"}, ensure_ascii=False)