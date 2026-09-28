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
