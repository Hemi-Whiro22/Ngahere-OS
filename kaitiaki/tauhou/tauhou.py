"""
Tauhou - Health Monitor & System Guardian
The silvereye that monitors system health, performance metrics, and alerts on issues with keen observation.
"""

import os
import json
import psutil
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

class Tauhou:
    """
    Tauhou - The Health Monitor
    Monitors system health, performance metrics, and alerts on issues with keen observation
    """
    
    def __init__(self):
        self.name = "Tauhou"
        self.role = "Health Monitor"
        self.health_logs = []
        self.performance_metrics = {}
        self.alert_thresholds = {
            "cpu_usage": 80,
            "memory_usage": 85,
            "disk_usage": 90
        }
    
    def monitor_health(self) -> str:
        """Tauhou monitors system health with keen observation"""
        timestamp = datetime.utcnow().isoformat()
        
        # Gather system metrics
        metrics = self._gather_system_metrics()
        
        # Analyze health status
        health_analysis = self._analyze_health(metrics)
        
        # Log health status
        health_log = {
            "timestamp": timestamp,
            "metrics": metrics,
            "health_status": health_analysis["status"],
            "alerts": health_analysis["alerts"],
            "overall_health": health_analysis["overall_health"]
        }
        
        self.health_logs.append(health_log)
        
        if health_analysis["status"] == "healthy":
            return f"🐦 Tauhou monitored health - all systems healthy at {timestamp}"
        elif health_analysis["status"] == "warning":
            return f"🐦 Tauhou detected warnings: {health_analysis['alerts']} at {timestamp}"
        else:
            return f"🐦 Tauhou detected critical issues: {health_analysis['alerts']} at {timestamp}"
    
    def _gather_system_metrics(self) -> dict:
        """Tauhou gathers system metrics with keen precision"""
        try:
            # CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Memory usage
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            # Disk usage
            disk = psutil.disk_usage('/')
            disk_percent = (disk.used / disk.total) * 100
            
            # System uptime
            uptime = psutil.boot_time()
            uptime_hours = (datetime.now().timestamp() - uptime) / 3600
            
            return {
                "cpu_usage": cpu_percent,
                "memory_usage": memory_percent,
                "disk_usage": disk_percent,
                "uptime_hours": uptime_hours,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            return {
                "error": f"Could not gather metrics: {str(e)}",
                "timestamp": datetime.utcnow().isoformat()
            }
    
    def _analyze_health(self, metrics: dict) -> dict:
        """Tauhou analyzes health with keen observation"""
        alerts = []
        status = "healthy"
        
        if "error" in metrics:
            return {
                "status": "error",
                "alerts": [metrics["error"]],
                "overall_health": "critical"
            }
        
        # Check CPU usage
        if metrics["cpu_usage"] > self.alert_thresholds["cpu_usage"]:
            alerts.append(f"High CPU usage: {metrics['cpu_usage']:.1f}%")
            status = "warning"
        
        # Check memory usage
        if metrics["memory_usage"] > self.alert_thresholds["memory_usage"]:
            alerts.append(f"High memory usage: {metrics['memory_usage']:.1f}%")
            status = "warning"
        
        # Check disk usage
        if metrics["disk_usage"] > self.alert_thresholds["disk_usage"]:
            alerts.append(f"High disk usage: {metrics['disk_usage']:.1f}%")
            status = "critical"
        
        # Determine overall health
        if status == "critical":
            overall_health = "critical"
        elif status == "warning":
            overall_health = "warning"
        else:
            overall_health = "healthy"
        
        return {
            "status": status,
            "alerts": alerts,
            "overall_health": overall_health
        }
    
    def set_alert_thresholds(self, thresholds: dict) -> str:
        """Tauhou sets alert thresholds for keen monitoring"""
        self.alert_thresholds.update(thresholds)
        timestamp = datetime.utcnow().isoformat()
        
        return f"🐦 Tauhou set alert thresholds for keen monitoring at {timestamp}"
    
    def get_health_summary(self) -> dict:
        """Tauhou's health monitoring summary"""
        if not self.health_logs:
            return {
                "kaitiaki": self.name,
                "status": "no_data",
                "message": "No health data available yet"
            }
        
        # Get latest health status
        latest_log = self.health_logs[-1]
        
        # Count health statuses
        healthy_count = len([log for log in self.health_logs if log.get("health_status") == "healthy"])
        warning_count = len([log for log in self.health_logs if log.get("health_status") == "warning"])
        critical_count = len([log for log in self.health_logs if log.get("health_status") == "critical"])
        
        return {
            "kaitiaki": self.name,
            "total_health_checks": len(self.health_logs),
            "healthy_checks": healthy_count,
            "warning_checks": warning_count,
            "critical_checks": critical_count,
            "latest_status": latest_log.get("health_status", "unknown"),
            "latest_metrics": latest_log.get("metrics", {}),
            "alert_thresholds": self.alert_thresholds
        }
    
    def get_status(self) -> dict:
        """Tauhou's overall status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "monitoring_keenly",
            "capabilities": [
                "health_monitoring",
                "performance_tracking",
                "alert_management",
                "system_observation",
                "metric_analysis"
            ],
            "health_summary": self.get_health_summary()
        }
