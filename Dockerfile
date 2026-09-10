# Python 3.12 বেস ইমেজ ব্যবহার করা
FROM python:3.12-slim

# ওয়ার্কিং ডিরেক্টরি সেট করা
WORKDIR /app

# প্রয়োজনীয় ডিপেন্ডেন্সি ফাইল কপি করা এবং ইনস্টল করা
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# প্রজেক্টের সমস্ত ফাইল কন্টেইনারে কপি করা
COPY . .

# এপিআই সার্ভারের পোর্ট ওপেন করা
EXPOSE 8000

# কন্টেইনার রান করার সময় ফাস্টএপিআই সার্ভার স্টার্ট করা
CMD ["python", "trustflow_server.py"]
