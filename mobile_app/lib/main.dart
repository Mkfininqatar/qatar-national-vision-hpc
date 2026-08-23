import 'package:flutter/material.dart';

void main() {
  runApp(const QatarNationalVisionApp());
}

class QatarNationalVisionApp extends StatelessWidget {
  const QatarNationalVisionApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Qatar National Vision HPC - Digital Twin',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: const Color(0xFF8A1538),
        scaffoldBackgroundColor: const Color(0xFF121212),
        cardColor: const Color(0xFF1E1E1E),
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF8A1538),
          secondary: Color(0xFFD4AF37),
        ),
      ),
      home: const DashboardScreen(),
    );
  }
}

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  int _selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xFF8A1538),
        title: const Text('QNV 2030 | Cardio-Neural Digital Twin Console'),
        actions: const [
          Padding(
            padding: EdgeInsets.symmetric(horizontal: 16.0),
            child: Center(
              child: Text(
                'HPC Cluster: Online',
                style: TextStyle(color: Colors.greenAccent, fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
      body: Row(
        children: [
          // Sidebar
          Container(
            width: 250,
            color: const Color(0xFF181818),
            child: ListView(
              children: [
                const DrawerHeader(
                  decoration: BoxDecoration(color: Color(0xFF8A1538)),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      Text(
                        'QNV 2030',
                        style: TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.bold),
                      ),
                      SizedBox(height: 4),
                      Text(
                        'Digital Twin Console',
                        style: TextStyle(color: Colors.white70, fontSize: 13),
                      ),
                    ],
                  ),
                ),
                ListTile(
                  leading: const Icon(Icons.dashboard),
                  title: const Text('Telemetry'),
                  selected: _selectedIndex == 0,
                  selectedTileColor: Colors.white10,
                  onTap: () => setState(() => _selectedIndex = 0),
                ),
                ListTile(
                  leading: const Icon(Icons.monitor_heart),
                  title: const Text('Cardio-Neural'),
                  selected: _selectedIndex == 1,
                  selectedTileColor: Colors.white10,
                  onTap: () => setState(() => _selectedIndex = 1),
                ),
                ListTile(
                  leading: const Icon(Icons.hub),
                  title: const Text('Nodes'),
                  selected: _selectedIndex == 2,
                  selectedTileColor: Colors.white10,
                  onTap: () => setState(() => _selectedIndex = 2),
                ),
              ],
            ),
          ),
          // Main Content
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'Doha Core Node Status & Metrics',
                    style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 20),
                  GridView.count(
                    crossAxisCount: 3,
                    crossAxisSpacing: 16,
                    mainAxisSpacing: 16,
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics,
                    childAspectRatio: 2.2,
                    children: const [
                      MetricCard(
                        title: 'Zero-Drift Pipeline',
                        value: 'Active',
                        subtitle: '0.00 µs',
                        icon: Icons.bolt,
                        color: Colors.greenAccent,
                      ),
                      MetricCard(
                        title: 'Coupled ODE Solver',
                        value: 'Running',
                        subtitle: 'Stable',
                        icon: Icons.settings_accessibility,
                        color: Colors.lightBlueAccent,
                      ),
                      MetricCard(
                        title: 'HPC Cluster Load',
                        value: '89.4%',
                        subtitle: 'Optimal Flow',
                        icon: Icons.memory,
                        color: Colors.orangeAccent,
                      ),
                    ],
                  ),
                  const SizedBox(height: 32),
                  Container(
                    height: 320,
                    decoration: BoxDecoration(
                      color: const Color(0xFF1E1E1E),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.white10),
                    ),
                    child: const Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.analytics_outlined, size: 64, color: Color(0xFFD4AF37)),
                          SizedBox(height: 16),
                          Text(
                            'Real-Time Cardio-Neural Axis Simulation Feed',
                            style: TextStyle(fontSize: 18, fontWeight: FontWeight.w500),
                          ),
                          SizedBox(height: 8),
                          Text(
                            'Telemetry stream connected successfully via WebSocket.',
                            style: TextStyle(color: Colors.white54, fontSize: 14),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class MetricCard extends StatelessWidget {
  final String title;
  final String value;
  final String subtitle;
  final IconData icon;
  final Color color;

  const MetricCard({
    Key? key,
    required this.title,
    required this.value,
    required this.subtitle,
    required this.icon,
    required this.color,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF1E1E1E),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.white10),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.between,
            children: [
              Text(title, style: const TextStyle(color: Colors.white70, fontSize: 14)),
              Icon(icon, color: color, size: 22),
            ],
          ),
          const SizedBox(height: 12),
          Row(
            mainAxisAlignment: MainAxisAlignment.between,
            children: [
              Text(value, style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: color)),
              Text(subtitle, style: const TextStyle(color: Colors.white54, fontSize: 12)),
            ],
          ),
        ],
      ),
    );
  }
}
@override
Widget build(BuildContext context) {
  return Scaffold(
    body: LayoutBuilder(
      builder: (context, constraints) {
        // স্ক্রিনের চওড়া বা উইডথ যদি ৯০০ পিক্সেলের বেশি হয় তবে ডেস্কটপ ভিউ দেখাবে
        if (constraints.maxWidth > 900) {
          return _buildDesktopLayout();
        } else {
          return _buildMobileLayout();
        }
      },
    ),
  );
}

// মনিটরের বড় স্ক্রিনের জন্য লেআউট (বামপাশে সাইডবার, ডানপাশে মেইন কনটেন্ট)
Widget _buildDesktopLayout() {
  return Row(
    children: [
      NavigationRail(
        backgroundColor: const Color(0xFF1E293B),
        selectedIndex: _currentIndex,
        onDestinationSelected: (index) => setState(() => _currentIndex = index),
        labelType: NavigationRailLabelType.all,
        destinations: const [
          NavigationRailDestination(icon: Icon(Icons.dashboard), label: Text('Telemetry')),
          NavigationRailDestination(icon: Icon(Icons.map), label: Text('Network Map')),
          NavigationRailDestination(icon: Icon(Icons.settings), label: Text('Settings')),
        ],
      ),
      Expanded(
        child: _pages[_currentIndex],
      ),
    ],
  );
}

// মোবাইলের জন্য সাধারণ বটম নেভিগেশন লেআউট
Widget _buildMobileLayout() {
  return Scaffold(
    appBar: AppBar(title: const Text('QNV 2030 Console')),
    body: _pages[_currentIndex],
    bottomNavigationBar: BottomNavigationBar(
      currentIndex: _currentIndex,
      onTap: (index) => setState(() => _currentIndex = index),
      items: const [
        BottomNavigationBarItem(icon: Icon(Icons.dashboard), label: 'Telemetry'),
        BottomNavigationBarItem(icon: Icon(Icons.map), label: 'Nodes'),
      ],
    ),
  );
}
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong2.dart';

class NetworkMapView extends StatelessWidget {
  const NetworkMapView({super.key});

  @override
  Widget build(BuildContext context) {
    return FlutterMap(
      options: MapOptions(
        initialCenter: LatLng(25.2854, 51.5310), // দোহার লোকেশন
        initialZoom: 11.0,
      ),
      children: [
        TileLayer(
          urlTemplate: 'https://openstreetmap.org{z}/{x}/{y}.png',
        ),
        MarkerLayer(
          markers: [
            Marker(
              point: LatLng(25.2854, 51.5310), // Doha Core Node
              child: const Icon(Icons.location_on, color: Colors.red, size: 40),
            ),
          ],
        ),
      ],
    );
  }
}
