import pytest
import yaml
import os

class TestCIPipeline:
    @pytest.fixture
    def config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'ci_pipeline.yml')
        with open(config_path) as f:
            return yaml.safe_load(f)

    def test_install_uses_pip3(self, config):
        install_steps = config['jobs']['install']['steps']
        install_cmd = [s for s in install_steps if s.get('name') == 'Install dependencies'][0]
        assert 'pip3' in install_cmd['run'] or 'pip install' not in install_cmd['run'], \
            "Should use pip3 for Python 3"

    def test_correct_job_order(self, config):
        test_needs = config['jobs']['test'].get('needs', [])
        assert 'build' in test_needs, "Test should run after build, not just install"

    def test_env_vars_in_test_step(self, config):
        test_steps = config['jobs']['test']['steps']
        run_step = [s for s in test_steps if s.get('name') == 'Run tests'][0]
        has_env = 'env' in run_step or 'DATABASE_URL' in str(run_step)
        assert has_env, "Test step should have DATABASE_URL env var"

    def test_deploy_conditional(self, config):
        deploy = config['jobs']['deploy']
        has_condition = 'if' in deploy
        assert has_condition, "Deploy should have a condition (if: success())"
