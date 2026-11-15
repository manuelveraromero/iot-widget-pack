# IoT & Mechatronics Web Widget Pack ⚡ [v1.0]

A high-performance, lightweight UI component library built for hardware engineers, robotics developers, and IoT makers. Designed with a clean **Dark Industrial / Cyberpunk** aesthetic, these widgets require zero heavy frameworks (pure HTML5, CSS3, and Vanilla JavaScript) and integrate seamlessly into any local or cloud telemetry dashboard.

---

## 🚀 Included Components

1. **Real-Time Waveform Oscilloscope (`<canvas>` based):** Optimized for streaming continuous analog signals, sensor feedback, or control loops with zero lag.
2. **Circular Gauge / Tachometer:** SVG-based dynamic progress indicator with automated warning color shifts (ideal for RPM, temperature, or pressure).
3. **PID Parameter & Setpoint Controller:** Clean interactive sliders with live numerical feedback for tuning control systems on the fly.
4. **System Status & Alarm Panel:** Virtual LED status matrix (`OK`, `WARN`, `CRIT`) paired with a live terminal event log.
5. **Battery & Power Monitor:** Dynamic progress bar tracking energy storage levels and instantaneous power consumption in Watts.

---

## 🛠️ Quick Start Guide

1. Clone or download the repository files into your project directory.
2. Include the core CSS variables and component markup inside your main HTML file.
3. Feed real-time data into the widgets using their clean JavaScript classes.

### Example Integration (JavaScript):

```javascript
// Initialize components
const osc = new RealtimeOscilloscope('oscCanvas');
const gauge = new CircularGauge('gaugeProgress', 'gaugeValue', 100);

// Update data dynamically from your WebSocket, MQTT, or Serial stream
function updateDashboard(incomingData) {
  osc.update(incomingData.sensorValue);
  gauge.setValue(incomingData.rpm);
}