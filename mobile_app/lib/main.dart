import 'package:flutter/material.dart';

void main() {
  runApp(const CardioNeuralApp());
}

class CardioNeuralApp extends StatelessWidget {
  const CardioNeuralApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'QNV Digital Twin Mobile',
      theme: ThemeData.dark().copyWith(
        primaryColor: Colors.blueAccent,
        scaffoldBackgroundColor: const Color(0xFF0B0F19),
      ),
      home: const DashboardScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  int _currentIndex = 0;

  final List<Widget> _pages = [
    const HomeTelemetryView(),
    const DigitalTwinView(),
    const SystemConfigView(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('QNV 2030 | Digital Twin Console'),
        backgroundColor: const Color(0xFF1E293B),
        elevation: 0,
      ),
      body: _pages[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        backgroundColor: const Color(0xFF1E293B),
        selectedItemColor: Colors.blueAccent,
        unselectedItemColor: Colors.grey,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.dashboard),
            label: 'Telemetry',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.monitor_heart),
            label: 'Cardio-Neural',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings_ethernet),
            label: 'Nodes',
          ),
        ],
      ),
    );
  }
}

class HomeTelemetryView extends StatelessWidget {
  const HomeTelemetryView({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: ListView(
        children: [
          const Text(
            'Doha Core Node Status',
            style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 16),
          _buildStatusCard('Zero-Drift Pipeline', 'Active (0.00 µs)', Colors.green),
          _buildStatusCard('Coupled ODE Solver', 'Running (Stable)', Colors.blue),
          _buildStatusCard('HPC Cluster Load', '14.2%', Colors.orange),
        ],
      ),
    );
  }

  Widget _buildStatusCard(String title, String status, Color color) {
    return Card(
      color: const Color(0xFF1E293B),
      margin: const EdgeInsets.only(bottom: 12),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(title, style: const TextStyle(fontSize: 16)),
            Chip(
              label: Text(status, style: const TextStyle(color: Colors.white)),
              backgroundColor: color,
            ),
          ],
        ),
      ),
    );
  }
}

class DigitalTwinView extends StatelessWidget {
  const DigitalTwinView({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Text(
        'Cardio-Neural Axis Simulation Feed\n[Live 3D/Graph Stream]',
        textAlign: TextAlign.center,
        style: TextStyle(fontSize: 18, color: Colors.grey),
      ),
    );
  }
}

class SystemConfigView extends StatelessWidget {
  const SystemConfigView({super.key});

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Text(
        'Node Routing & ISACA Compliance Controls',
        textAlign: TextAlign.center,
        style: TextStyle(fontSize: 18, color: Colors.grey),
      ),
    );
  }
} import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';

class TelemetryService {
  late WebSocketChannel _channel;
  
  // দোহা কোর নোড বা HPC ক্লাস্টারের লাইভ স্ট্রিম এন্ডপয়েন্ট
  void connectToDohaCore() {
    _channel = WebSocketChannel.connect(
      Uri.parse('wss://doha-core-telemetry.qnv2030.internal/ws'),
    );
  }

  Stream<Map<String, dynamic>> get telemetryStream {
    return _channel.stream.map((message) {
      final decoded = jsonDecode(message);
      return {
        'cpuLoad': decoded['cpu_load'] ?? 0.0,
        'driftTime': decoded['drift_time'] ?? '0.00 µs',
        'nodeStatus': decoded['status'] ?? 'Active',
      };
    });
  }

  void dispose() {
    _channel.sink.close();
  }
}
