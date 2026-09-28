import logging
import urllib.request
import json
from typing import Dict, Any

logger = logging.getLogger("WebhookNotifier")

class WebhookNotifier:
    """
    টেলিমেট্রি অ্যালার্ট বা ক্রিটিক্যাল সিস্টেম ইভেন্টের জন্য এক্সটার্নাল ওয়েবহুক নোটিফিকেশন হ্যান্ডলার।
    """
    def __init__(self, webhook_url: str = None):
        # যদি নির্দিষ্ট কোনো প্ল্যাটফর্ম (যেমন Zangi বা কাস্টম এন্ডপয়েন্ট) হয়, তার URL এখানে সেট হবে
        self.webhook_url = webhook_url or "https://api.zangi.com/v1/webhook" # উদাহরণস্বরূপ এন্ডপয়েন্ট

    def send_alert(self, alert_messages: list, metrics: Dict[str, Any]) -> bool:
        """
        ক্রিটিক্যাল অ্যালার্টগুলো ওয়েবহুকের মাধ্যমে এক্সটার্নাল চ্যানেলে প্রেরণ করে।
        """
        if not self.webhook_url:
            logger.warning("Webhook URL is not configured. Skipping external notification.")
            return False

        payload = {
            "source": "Qatar National Vision HPC Telemetry",
            "status": "CRITICAL_ALERT",
            "messages": alert_messages,
            "metrics": metrics
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
                else:
                    logger.error(f"Failed to send webhook. Status code: {response.status}")
                    return False
                    
        except Exception as e:
            logger.error(f"Error connecting to webhook endpoint: {e}")
            return False
