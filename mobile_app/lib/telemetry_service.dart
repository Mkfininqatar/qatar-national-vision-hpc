import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';

class TelemetryService {
  late WebSocketChannel _channel;
  
  // Doha Core Node Telemetry Endpoint
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
