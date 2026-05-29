import pytest
from src.task_manager import TaskManager

def test_create_task():
    manager = TaskManager()
    task = manager.create_task("Entregar Carga A", "Rota expressa para SP")
    assert task["id"] == 1
    assert task["title"] == "Entregar Carga A"
    assert task["status"] == "A Fazer"

def test_create_task_invalid_title():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.create_task("", "Sem título")

def test_update_status():
    manager = TaskManager()
    manager.create_task("Fretamento B", "Análise de custos")
    updated = manager.update_task_status(1, "Em Progresso")
    assert updated["status"] == "Em Progresso"