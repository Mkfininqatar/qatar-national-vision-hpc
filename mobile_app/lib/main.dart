import 'package:flutter/material.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

void main() {
  runApp(const QatarNationalVisionApp());
}

class QatarNationalVisionApp extends StatelessWidget {
  const QatarNationalVisionApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Qatar National Vision HPC',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: const Color(0xFF8A1538), // Maroon (Qatar Flag Color)
        scaffoldBackgroundColor: const Color(0xFF121212),
        cardColor: const Color(0xFF1E1E1E),
        colorScheme: ColorScheme.dark(
          primary: const Color(0xFF8A1538),
          secondary: const Color(0xFFD4AF37),
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
    final bool isDesktop = MediaQuery.of(context).size.width > 800;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xFF8A1538),
        title: const Text('Qatar National Vision HPC'),
        actions: [
          IconButton(
            icon: const Icon(Icons.notifications_outlined),
            onPressed: () {},
          ),
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 16.0),
            child: CircleAvatar(
              backgroundColor: Colors.white24,
              child: Icon(Icons.person, color: Colors.white),
            ),
          ),
        ],
      ),
      drawer: isDesktop ? null : _buildSidebar(context),
      body: Row(
        children: [
          if (isDesktop) _buildSidebar(context),
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Key Metrics Header
                  const Text(
                    'Key Metrics',
                    style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 16),
                  
                  // Metrics Cards Grid
                  LayoutBuilder(
                    builder: (context, constraints) {
                      return GridView.count(
                        crossAxisCount: constraints.maxWidth > 900 ? 3 : 1,
                        crossAxisSpacing: 16,
                        mainAxisSpacing: 16,
                        shrinkWrap: true,
                        physics: const NeverScrollableScrollPhysics,
                        childAspectRatio: 2.5,
                        children: const [
                          MetricCard(
                            title: 'HPC Cluster Status',
                            value: '89%',
                            subtitle: 'Operational',
                            icon: Icons.computer,
                            progress: 0.89,
                          ),
                          MetricCard(
                            title: 'Job Throughput',
                            value: 'Live',
                            subtitle: 'Stable Flow',
                            icon: Icons.show_chart,
                            isChart: true,
                          ),
                          MetricCard(
                            title: 'Active Nodes',
                            value: '341',
                            subtitle: 'Connected',
                            icon: Icons.hub,
                          ),
                        ],
                      );
                    },
                  ),
                  const SizedBox(height: 32),

                  // Map / Digital Twin Overview Section
                  Container(
                    height: 300,
                    decoration: BoxDecoration(
                      color: const Color(0xFF1E1E1E),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.white10),
                    ),
                    child: Stack(
                      children: [
                        Center(
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(Icons.map, size: 64, color: Colors.white54),
                              const SizedBox(height: 12),
                              const Text(
                                'Digital Twin Node Topology (Doha Cluster)',
                                style: TextStyle(color: Colors.white70, fontSize: 16),
                              ),
                              const SizedBox(height: 8),
                              ElevatedButton.icon(
                                style: ElevatedButton.styleFrom(
                                  backgroundColor: const Color(0xFF8A1538),
                                ),
                                icon: const Icon(Icons.refresh),
                                label: const Text('Sync Telemetry'),
                                onPressed: () {},
                              ),
                            ],
                          ),
                        ),
                        Positioned(
                          top: 16,
                          left: 16,
                          child: Container(
                            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                            decoration: BoxDecoration(
                              color: Colors.black54,
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: const Text('Live Feed: Active', style: TextStyle(color: Colors.greenAccent)),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 32),

                  // Recent Activity Log
                  const Text(
                    'Recent Activity Log',
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 16),
                  Container(
                    decoration: BoxDecoration(
                      color: const Color(0xFF1E1E1E),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Column(
                      children: const [
                        ActivityTile(
                          title: 'Job #1034 Completed',
                          time: '2m ago',
                          icon: Icons.check_circle,
                          color: Colors.green,
                        ),
                        Divider(height: 1, color: Colors.white10),
                        ActivityTile(
                          title: 'New Node Added - Node 341',
                          time: '15m ago',
                          icon: Icons.add_circle,
                          color: Colors.blue,
                        ),
                        Divider(height: 1, color: Colors.white10),
                        ActivityTile(
                          title: 'Cluster Maintenance Scheduled',
                          time: '1h ago',
                          icon: Icons.schedule,
                          color: Colors.orange,
                        ),
                      ],
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

  Widget _buildSidebar(BuildContext context) {
    return Container(
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
                  'Cardio-Neural Digital Twin',
                  style: TextStyle(color: Colors.white70, fontSize: 13),
                ),
              ],
            ),
          ),
          ListTile(
            leading: const Icon(Icons.dashboard),
            title: const Text('Dashboard'),
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
          ListTile(
            leading: const Icon(Icons.analytics),
            title: const Text('Analytics'),
            selected: _selectedIndex == 3,
            selectedTileColor: Colors.white10,
            onTap: () => setState(() => _selectedIndex = 3),
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
  final double? progress;
  final bool isChart;

  const MetricCard({
    Key? key,
    required this.title,
    required this.value,
    required this.subtitle,
    required this.icon,
    this.progress,
    this.isChart = false,
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
              Icon(icon, color: const Color(0xFFD4AF37), size: 20),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.between,
            children: [
              Text(value, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
              Text(subtitle, style: const TextStyle(color: Colors.greenAccent, fontSize: 12)),
            ],
          ),
          if (progress != null) ...[
            const SizedBox(height: 8),
            LinearProgressIndicator(
              value: progress,
              backgroundColor: Colors.white10,
              color: const Color(0xFF8A1538),
            ),
          ],
        ],
      ),
    );
  }
}

class ActivityTile extends StatelessWidget {
  final String title;
  final String time;
  final IconData icon;
  final Color color;

  const ActivityTile({
    Key? key,
    required this.title,
    required this.time,
    required this.icon,
    required this.color,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: Icon(icon, color: color),
      title: Text(title, style: const TextStyle(fontSize: 14)),
      trailing: Text(time, style: const TextStyle(color: Colors.white54, fontSize: 12)),
    );
  }
}
