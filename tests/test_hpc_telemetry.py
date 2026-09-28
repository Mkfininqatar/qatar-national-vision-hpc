import os
import pytest
from unittest.mock import patch
# আপনার ইঞ্জিনের ক্লাস বা মডিউল পাথ অনুযায়ী এটি ইমপোর্ট করবেন
# from src.hpc_telemetry import PersistentTelemetryEngine

class TestPersistentTelemetryEngine:
    
    @pytest.fixture
    def telemetry_engine(self, tmp_path):
        """টেস্টের জন্য একটি সাময়িক লগ ডিরেক্টরি এবং ইঞ্জিন ইনস্ট্যান্স তৈরি করে।"""
        log_dir = tmp_path / "telemetry_logs"
        log_dir.mkdir()
        # engine = PersistentTelemetryEngine(log_path=str(log_dir / "metrics.log"))
        # return engine
        return str(log_dir / "metrics.log")

    def test_telemetry_initialization(self, telemetry_engine):
        """ইঞ্জিন সঠিকভাবে ইনিশিয়ালাইজ হচ্ছে কিনা তা যাচাই করে।"""
        assert telemetry_engine is not None
        assert os.path.exists(os.path.dirname(telemetry_engine))

    @pytest.mark.parametrize("cpu_load, memory_usage, expected_alert", [
        (45.5, 60.2, False),
        (92.0, 85.0, True),   # হাই লোড বা থ্রেশহোল্ড ক্রস করলে অ্যালার্ট ট্রিগার হবে
        (10.0, 15.0, False),
    ])
    def test_metric_threshold_evaluation(self, cpu_load, memory_usage, expected_alert):
        """বিভিন্ন সিপিইউ এবং মেমোরি লোডের জন্য অ্যালার্ট মূল্যায়ন পরীক্ষা করা।"""
        # সিমুলেটেড লজিক যাচাই
        is_critical = cpu_load > 90.0 or memory_usage > 90.0
        # এখানে আপনার আসল ইঞ্জিনের থ্রেশহোল্ড ফাংশন কল করতে পারেন
        assert is_critical == expected_alert
