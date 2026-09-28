import logging
import sys

# কনফিগারেশন লগিং
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("TelemetryAlertEngine")

class RealTimeAlertEngine:
    def __init__(self, cpu_threshold: float = 90.0, memory_threshold: float = 90.0):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold

    def evaluate_metrics(self, cpu_load: float, memory_usage: float) -> bool:
        """
        সিপিইউ এবং মেমোরি মেট্রিকস মূল্যায়ন করে এবং থ্রেশহোল্ড ক্রস করলে অ্যালার্ট ট্রিগার করে।
        """
        alert_triggered = False

        if cpu_load > self.cpu_threshold:
            logger.warning(f"🚨 CRITICAL ALERT: CPU load reached {cpu_load}% (Threshold: {self.cpu_threshold}%)")
            alert_triggered = True

        if memory_usage > self.memory_threshold:
            logger.warning(f"🚨 CRITICAL ALERT: Memory usage reached {memory_usage}% (Threshold: {self.memory_threshold}%)")
            alert_triggered = True

        if not alert_triggered:
            logger.info(f"System status normal. CPU: {cpu_load}%, Memory: {memory_usage}%")

        return alert_triggered
import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional

# কনফিগারেশন লগিং সেটআপ
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger("TelemetryAlertEngine")

class PersistentTelemetryAlertEngine:
    """
    HPC টেলিমেট্রি এবং মেট্রিক লগিংয়ের জন্য পার্সিস্টেন্ট অ্যালার্ট ইঞ্জিন।
    থ্রেশহোল্ড অতিক্রম করলে বা সিস্টেম ফেইল করলে তাৎক্ষণিক নোটিফিকেশন ও লগ তৈরি করে।
    """
    def __init__(
        self, 
        log_file_path: str = "logs/telemetry_metrics.log",
        cpu_threshold: float = 90.0, 
        memory_threshold: float = 90.0
    ):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.log_file_path = log_file_path
        
        # লগ ডিরেক্টরি তৈরি নিশ্চিত করা
        log_dir = os.path.dirname(self.log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

    def evaluate_and_persist(self, metrics: Dict[str, Any]) -> bool:
        """
        মেট্রিকস ডেটা ইনপুট নিয়ে থ্রেশহোল্ড চেক করে, ফাইলে সেভ করে এবং অ্যালার্ট ট্রিগার করে।
        """
        timestamp = datetime.utcnow().isoformat()
        cpu_load = metrics.get("cpu_load", 0.0)
        memory_usage = metrics.get("memory_usage", 0.0)
        gpu_temp = metrics.get("gpu_temp", 0.0)

        alert_triggered = False
        alert_messages = []

        if cpu_load > self.cpu_threshold:
            msg = f"CRITICAL: CPU load exceeded threshold -> {cpu_load}% (Limit: {self.cpu_threshold}%)"
            logger.warning(msg)
            alert_messages.append(msg)
            alert_triggered = True

        if memory_usage > self.memory_threshold:
            msg = f"CRITICAL: Memory usage exceeded threshold -> {memory_usage}% (Limit: {self.memory_threshold}%)"
            logger.warning(msg)
            alert_messages.append(msg)
            alert_triggered = True

        # পার্সিস্টেন্ট লগে ডেটা এবং অ্যালার্ট স্ট্যাটাস সেভ করা
        log_entry = (
            f"[{timestamp}] STATUS: {'ALERT' if alert_triggered else 'NORMAL'} | "
            f"CPU: {cpu_load}% | Memory: {memory_usage}% | GPU Temp: {gpu_temp}°C\n"
        )
        
        try:
            with open(self.log_file_path, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            logger.error(f"Failed to write telemetry log to file: {e}")

        if not alert_triggered:
            logger.info(f"Telemetry metrics normal. CPU: {cpu_load}%, Memory: {memory_usage}%")

        return alert_triggered
from src.telemetry_alert_engine import PersistentTelemetryAlertEngine

engine = PersistentTelemetryAlertEngine()
engine.evaluate_and_persist({"cpu_load": 85.5, "memory_usage": 60.2, "gpu_temp": 72.0})
import os
import logging
import urllib.request
import json
from datetime import datetime
from typing import Dict, Any, Optional

# কনফিগারেশন লগিং সেটআপ
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger("TelemetryAlertEngine")

class PersistentTelemetryAlertEngine:
    """
    HPC টেলিমেট্রি এবং মেট্রিক লগিংয়ের জন্য পার্সিস্টেন্ট অ্যালার্ট ও ওয়েবহুক নোটিফিকেশন ইঞ্জিন।
    """
    def __init__(
        self, 
        log_file_path: str = "logs/telemetry_metrics.log",
        cpu_threshold: float = 90.0, 
        memory_threshold: float = 90.0,
        webhook_url: Optional[str] = None
    ):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold
        self.log_file_path = log_file_path
        self.webhook_url = webhook_url or os.getenv("TELEMETRY_WEBHOOK_URL")
        
        # লগ ডিরেক্টরি তৈরি নিশ্চিত করা
        log_dir = os.path.dirname(self.log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

    def _send_webhook(self, alert_messages: list, metrics: Dict[str, Any]) -> bool:
        """প্রাইভেট মেথড: থ্রেশহোল্ড ক্রস করলে ওয়েবহুকে নোটিফিকেশন পাঠায়।"""
        if not self.webhook_url:
            return False

        payload = {
            "source": "Qatar National Vision HPC Telemetry",
            "status": "CRITICAL_ALERT",
            "messages": alert_messages,
            "metrics": metrics,
            "timestamp": datetime.utcnow().isoformat()
        }

        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                self.webhook_url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    logger.info("External webhook notification sent successfully.")
                    return True
        except Exception as e:
            logger.error(f"Error connecting to webhook endpoint: {e}")
        return False

    def evaluate_and_persist(self, metrics: Dict[str, Any]) -> bool:
        """
        মেট্রিকস ডেটা ইনপুট নিয়ে থ্রেশহোল্ড চেক করে, ফাইলে সেভ করে এবং দরকার হলে ওয়েবহুক ট্রিগার করে।
        """
        timestamp = datetime.utcnow().isoformat()
        cpu_load = metrics.get("cpu_load", 0.0)
        memory_usage = metrics.get("memory_usage", 0.0)
        gpu_temp = metrics.get("gpu_temp", 0.0)

        alert_triggered = False
        alert_messages = []

        if cpu_load > self.cpu_threshold:
            msg = f"CRITICAL: CPU load exceeded threshold -> {cpu_load}% (Limit: {self.cpu_threshold}%)"
            logger.warning(msg)
            alert_messages.append(msg)
            alert_triggered = True

        if memory_usage > self.memory_threshold:
            msg = f"CRITICAL: Memory usage exceeded threshold -> {memory_usage}% (Limit: {self.memory_threshold}%)"
            logger.warning(msg)
            alert_messages.append(msg)
            alert_triggered = True

        # পার্সিস্টেন্ট লগে ডেটা এবং অ্যালার্ট স্ট্যাটাস সেভ করা
        log_entry = (
            f"[{timestamp}] STATUS: {'ALERT' if alert_triggered else 'NORMAL'} | "
            f"CPU: {cpu_load}% | Memory: {memory_usage}% | GPU Temp: {gpu_temp}°C\n"
        )
        
        try:
            with open(self.log_file_path, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            logger.error(f"Failed to write telemetry log to file: {e}")

        # অ্যালার্ট ট্রিগার হলে স্বয়ংক্রিয়ভাবে ওয়েবহুক কল হবে
        if alert_triggered:
            self._send_webhook(alert_messages, metrics)
        else:
            logger.info(f"Telemetry metrics normal. CPU: {cpu_load}%, Memory: {memory_usage}%")

        return alert_triggered
