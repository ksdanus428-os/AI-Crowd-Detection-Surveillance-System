import React, { useEffect, useState } from "react";
import { StyleSheet, Text, View, ScrollView } from "react-native";

const SERVER_IP = "192.168.1.103"; // your laptop IP

export default function App() {
  const [peopleCount, setPeopleCount] = useState(0);
  const [crowdDetected, setCrowdDetected] = useState(false);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch(`http://${SERVER_IP}:5000/status`)
        .then(res => res.json())
        .then(data => {
          setPeopleCount(data.people_count);
          setCrowdDetected(data.crowd_detected);
        }).catch(err => console.log("Status Error:", err));

      fetch(`http://${SERVER_IP}:5000/alerts`)
        .then(res => res.json())
        .then(data => setAlerts(data))
        .catch(err => console.log("Alert Error:", err));
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>AI Surveillance</Text>
      <Text style={styles.count}>{peopleCount}</Text>
      <Text style={styles.label}>People Detected</Text>
      {crowdDetected && <Text style={styles.crowd}>CROWD DETECTED!</Text>}

      <Text style={styles.alertTitle}>Snapshot Alerts</Text>
      <ScrollView style={styles.alertBox}>
        {alerts.map((alert, index) => (
          <View key={index} style={styles.alertItem}>
            <Text style={styles.alertText}>
              Person {alert.person_id} - {alert.time}s at {alert.timestamp}
            </Text>
          </View>
        ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#111", alignItems: "center", paddingTop: 60 },
  title: { fontSize: 24, color: "#00ffcc", marginBottom: 20 },
  count: { fontSize: 50, color: "#00ffcc" },
  label: { fontSize: 18, color: "#aaa" },
  crowd: { fontSize: 22, color: "#ff4444", marginTop: 10 },
  alertTitle: { fontSize: 20, color: "#ff4444", marginBottom: 10 },
  alertBox: { width: "90%" },
  alertItem: { backgroundColor: "#333", padding: 10, borderRadius: 10, marginBottom: 10 },
  alertText: { color: "#fff" },
});