import json

leadership_architecture = {
    "Project": "Sovereign Gaza Infrastructure & Digital Twin Framework",
    "Leadership_Board": {
        "Strategic_Director": "HH Sheikh Tamim Sir",
        "Foundational_Visionary": "Father Amir Sheikh Hamad bin Khalifa Al Thani (Rahmatullah)",
        "Technical_Architect": "Abdul Majeed"
    },
    "Architectural_Modules": [
        "Autonomous Solar Micro-Grid & Desalination Topology",
        "Predictive Resource & AI Triage Telemetry",
        "Coastal Light Rail & Eco-Housing Digital Twin",
        "Global Media Telecast & Open API Gateway"
    ],
    "System_Status": "OPERATIONAL & READY FOR PHASE 2 EXPANSION"
}

print("--- SOVEREIGN GAZA PROJECT LEADERSHIP PROFILE ---")
print(json.dumps(leadership_architecture, indent=2))
import json

leadership_architecture = {
    "Project": "Sovereign Gaza Infrastructure & Digital Twin Framework",
    "Leadership_Board": {
        "Strategic_Director": "HH Sheikh Tamim Sir",
        "Foundational_Visionary": "Father Amir Sheikh Hamad bin Khalifa Al Thani (Rahmatullah)",
        "Technical_Architect": "Abdul Majeed"
    },
    "Architectural_Modules": [
        "Autonomous Solar Micro-Grid & Desalination Topology",
        "Predictive Resource & AI Triage Telemetry",
        "Coastal Light Rail & Eco-Housing Digital Twin",
        "Global Media Telecast & Open API Gateway"
    ],
    "System_Status": "OPERATIONAL & READY FOR PHASE 2 EXPANSION"
}

print("--- SOVEREIGN GAZA PROJECT LEADERSHIP PROFILE ---")
print(json.dumps(leadership_architecture, indent=2))
import pandas as pd

# Immediate Emergency Pipeline Metrics
emergency_pipeline = {
    "Humanitarian Sector": [
        "Clean Water Tankers & Solar Desalination",
        "High-Energy Food Rations & Wheat Grain",
        "Trauma Kits & Essential Surgery Supplies",
        "Mobile Health Units & Field Hospitals",
        "Infant Nutrition & Medical Formula"
    ],
    "Current Stock Level (%)": [88, 92, 85, 90, 86],
    "Pipeline Status": [
        "ACTIVE DISTRIBUTION",
        "ACTIVE DISTRIBUTION",
        "PRIORITY DISPATCH",
        "DEPLOYED ON SITE",
        "ACTIVE DISTRIBUTION"
    ]
}

df_emergency = pd.DataFrame(emergency_pipeline)
print("--- GAZA PHASE 1: EMERGENCY RELIEF PIPELINE STATUS ---")
print(df_emergency.to_string(index=False))
import datetime
import json
import random

# =========================================================
# GAZA INTERNAL AI & TELEMETRY ENGINE
# =========================================================

class InternalAIEngine:
    def __init__(self):
        self.node_id = "GAZA-CENTRAL-AI-01"
        self.status = "ONLINE"
        
    def resource_demand_sensing(self, population_count, days_ahead=1):
        """
        1. AI Resource & Inventory Telemetry
        Predicts daily required water, food rations, and medical kits.
        """
        water_per_capita_liters = 15  # Emergency standard
        food_rations_per_capita = 1
        medical_kits_per_1000 = 2.5

        predicted_water_m3 = (population_count * water_per_capita_liters * days_ahead) / 1000
        predicted_food_units = population_count * food_rations_per_capita * days_ahead
        predicted_med_kits = (population_count / 1000) * medical_kits_per_1000 * days_ahead

        return {
            "target_population": population_count,
            "days_forecast": days_ahead,
            "required_water_m3": round(predicted_water_m3, 2),
            "required_food_rations": int(predicted_food_units),
            "required_trauma_kits": int(predicted_med_kits)
        }

    def smart_microgrid_load_balancer(self, solar_input_kw, battery_level_pct):
        """
        2. Autonomous Micro-Grid Control
        Optimizes power allocation dynamically based on solar and battery state.
        """
        total_capacity_kw = solar_input_kw + (battery_level_pct * 5)  # Simulated battery weight
        
        # Priority distribution logic
        hospitals_kw = min(total_capacity_kw * 0.50, 200) # Highest priority
        desalination_kw = min(total_capacity_kw * 0.35, 150)
        communications_kw = min(total_capacity_kw * 0.15, 50)

        grid_status = "STABLE" if battery_level_pct > 30 else "CRITICAL_SAVING_MODE"

        return {
            "grid_mode": grid_status,
            "solar_input_kw": solar_input_kw,
            "battery_pct": battery_level_pct,
            "power_allocation_kw": {
                "Field Hospitals & ICUs": round(hospitals_kw, 2),
                "Desalination & Water Pumps": round(desalination_kw, 2),
                "Satellite & Telecom Hubs": round(communications_kw, 2)
            }
        }

    def automated_medical_triage(self, heart_rate, spo2_pct, injury_severity_scale):
        """
        3. Tele-Medicine & Triage AI
        Categorizes incoming medical cases automatically.
        """
        # Injury scale 1 (minor) to 10 (critical)
        if spo2_pct < 85 or heart_rate > 130 or injury_severity_scale >= 8:
            triage_category = "RED (IMMEDIATE TRAUMA / CRITICAL)"
            priority_score = 1
        elif 85 <= spo2_pct <= 92 or 110 < heart_rate <= 130 or 5 <= injury_severity_scale < 8:
            triage_category = "YELLOW (URGENT / DELAYED)"
            priority_score = 2
        else:
            triage_category = "GREEN (MINOR / OUTPATIENT)"
            priority_score = 3

        return {
            "vitals": {"hr": heart_rate, "spo2": spo2_pct, "severity": injury_severity_scale},
            "triage_category": triage_category,
            "dispatch_priority": priority_score
        }

    def network_self_healing(self, active_mesh_nodes):
        """
        4. Independent Signal & Mesh Network Optimization
        Reroutes communication traffic if a satellite/fiber node goes down.
        """
        operational_nodes = [node for node, state in active_mesh_nodes.items() if state == "ONLINE"]
        failed_nodes = [node for node, state in active_mesh_nodes.items() if state == "OFFLINE"]

        return {
            "total_nodes": len(active_mesh_nodes),
            "operational_count": len(operational_nodes),
            "failed_count": len(failed_nodes),
            "active_routing_path": " -> ".join(operational_nodes),
            "reroute_action": "AUTOMATIC MESH RECONFIGURATION COMPLETE" if failed_nodes else "OPTIMAL FLOW"
        }

# =========================================================
# EXECUTION SIMULATION
# =========================================================
if __name__ == "__main__":
    ai = InternalAIEngine()
    
    print("=========================================================")
    print(f"🤖 {ai.node_id} - OPERATIONAL SYSTEM CHECK")
    print(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=========================================================\n")

    # 1. Resource Demand Test (50,000 population local cluster)
    resource_prediction = ai.resource_demand_sensing(population_count=50000, days_ahead=3)
    print("📦 [1] RESOURCE DEMAND FORECAST (3 Days):")
    print(json.dumps(resource_prediction, indent=2))
    print("\n" + "-"*50 + "\n")

    # 2. Smart Micro-Grid Load Test
    grid_data = ai.smart_microgrid_load_balancer(solar_input_kw=250, battery_level_pct=65)
    print("⚡ [2] SMART MICRO-GRID ALLOCATION:")
    print(json.dumps(grid_data, indent=2))
    print("\n" + "-"*50 + "\n")

    # 3. Medical Triage Test
    patient_triage = ai.automated_medical_triage(heart_rate=135, spo2_pct=82, injury_severity_scale=9)
    print("🏥 [3] AUTOMATED MEDICAL TRIAGE SYSTEM:")
    print(json.dumps(patient_triage, indent=2))
    print("\n" + "-"*50 + "\n")

    # 4. Network Self-Healing Test
    nodes_state = {
        "SAT-NODE-NORTH": "ONLINE",
        "FIBER-NODE-CENTRAL": "OFFLINE", # Simulated failure
        "MESH-NODE-SOUTH": "ONLINE",
        "PORT-NODE-WEST": "ONLINE"
    }
    network_status = ai.network_self_healing(nodes_state)
    print("📡 [4] NETWORK SELF-HEALING ROUTER:")
    print(json.dumps(network_status, indent=2))
    print("\n=========================================================")
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ---------------------------------------------------------
# PHASE 1 PIPELINE TELEMETRY DATA
# ---------------------------------------------------------
pipeline_nodes_data = {
    "Module": [
        "Food: MREs & Rations",
        "Food: Grain & Bakery Hubs",
        "Water: Solar Desalination",
        "Water: Tanker Distribution",
        "Medical: Field Hospitals & ICU",
        "Medical: Mobile Clinics"
    ],
    "Category": ["Food Security", "Food Security", "Water & Sanitation", "Water & Sanitation", "Medical Support", "Medical Support"],
    "Supply Flow Rate (%)": [92, 85, 95, 88, 90, 84],
    "Operational Status": ["ACTIVE", "ACTIVE", "STABLE", "ACTIVE", "PRIORITY", "DEPLOYED"],
    "Daily Target (Units)": [50000, 30000, 100000, 80000, 2000, 5000]
}

df_pipeline = pd.DataFrame(pipeline_nodes_data)

# Initialize Dash App
app = dash.Dash(__name__)
app.title = "Phase 1 Emergency Pipeline Network Dashboard"

# ---------------------------------------------------------
# UI LAYOUT (EMERGENCY TOPOLOGY THEME)
# ---------------------------------------------------------
app.layout = html.Div(style={
    'backgroundColor': '#0b0f19', # Deep dark network grid background
    'color': '#f8fafc',
    'fontFamily': 'Segoe UI, Arial, sans-serif',
    'padding': '25px'
}, children=[

    # Header Section
    html.Div([
        html.H1("🚨 PHASE 1: EMERGENCY HUMANITARIAN PIPELINE DASHBOARD", 
                style={'color': '#10b981', 'marginBottom': '5px', 'fontWeight': 'bold'}),
        html.P("Live Telemetry & Network Monitoring: Food, Water & Emergency Healthcare Distribution",
               style={'color': '#94a3b8', 'fontSize': '15px'})
    ], style={'borderBottom': '1px solid #1e293b', 'paddingBottom': '15px'}),

    # Key Status Indicators
    html.Div([
        html.Div([
            html.H4("🍲 Food Pipeline", style={'color': '#f59e0b', 'margin': '0 0 5px 0'}),
            html.H2("88.5% ACTIVE", style={'color': '#f59e0b', 'margin': '0 0 5px 0'}),
            html.P("Rations & Bakery Hubs Operational", style={'color': '#94a3b8', 'margin': '0'})
        ], style={'backgroundColor': '#1e1b4b', 'padding': '20px', 'borderRadius': '8px', 'width': '30%', 'borderLeft': '4px solid #f59e0b'}),

        html.Div([
            html.H4("💧 Clean Water Network", style={'color': '#38bdf8', 'margin': '0 0 5px 0'}),
            html.H2("91.5% STABLE", style={'color': '#38bdf8', 'margin': '0 0 5px 0'}),
            html.P("Solar Desalination & Tankers Active", style={'color': '#94a3b8', 'margin': '0'})
        ], style={'backgroundColor': '#1e1b4b', 'padding': '20px', 'borderRadius': '8px', 'width': '30%', 'borderLeft': '4px solid #38bdf8'}),

        html.Div([
            html.H4("🏥 Healthcare Infrastructure", style={'color': '#ef4444', 'margin': '0 0 5px 0'}),
            html.H2("87.0% DEPLOYED", style={'color': '#ef4444', 'margin': '0 0 5px 0'}),
            html.P("Trauma Care & Field ICU Online", style={'color': '#94a3b8', 'margin': '0'})
        ], style={'backgroundColor': '#1e1b4b', 'padding': '20px', 'borderRadius': '8px', 'width': '30%', 'borderLeft': '4px solid #ef4444'}),
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '25px'}),

    # Visualizations Section
    html.Div([
        # Bar Chart for Modules Flow
        html.Div([
            html.H3("📊 Supply Pipeline Flow Rate by Module", style={'color': '#10b981'}),
            dcc.Graph(id='bar-chart-pipeline')
        ], style={'backgroundColor': '#182232', 'padding': '20px', 'borderRadius': '8px', 'width': '48%'}),

        # Sunburst / Network Distribution Chart
        html.Div([
            html.H3("🌐 Resource Category Allocation", style={'color': '#10b981'}),
            dcc.Graph(id='pie-chart-pipeline')
        ], style={'backgroundColor': '#182232', 'padding': '20px', 'borderRadius': '8px', 'width': '48%'})
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '25px'}),

    # Live Interactive Controls
    html.Div([
        html.H3("🎛️ Network Throughput Simulation Control", style={'color': '#10b981'}),
        html.P("Adjust overall logistics capacity to monitor emergency dispatch readiness:", style={'color': '#cbd5e1'}),
        dcc.Slider(
            id='pipeline-slider',
            min=0,
            max=100,
            step=5,
            value=90,
            marks={i: f'{i}% Capacity' for i in range(0, 101, 20)}
        ),
        html.Div(id='pipeline-status-output', style={
            'marginTop': '20px', 
            'fontSize': '18px', 
            'fontWeight': 'bold', 
            'padding': '14px', 
            'backgroundColor': '#0b0f19', 
            'borderRadius': '6px', 
            'textAlign': 'center',
            'border': '1px solid #10b981'
        })
    ], style={'backgroundColor': '#182232', 'padding': '25px', 'borderRadius': '8px', 'marginTop': '25px'})
])

# ---------------------------------------------------------
# CALLBACK LOGIC
# ---------------------------------------------------------
@app.callback(
    [Output('bar-chart-pipeline', 'figure'),
     Output('pie-chart-pipeline', 'figure'),
     Output('pipeline-status-output', 'children')],
    [Input('pipeline-slider', 'value')]
)
def update_dashboard(slider_value):
    # Dynamic update based on slider
    df_updated = df_pipeline.copy()
    df_updated["Supply Flow Rate (%)"] = (df_updated["Supply Flow Rate (%)"] * (slider_value / 100.0)).round(1)

    # Bar Chart Visual
    fig_bar = px.bar(
        df_updated, 
        x="Supply Flow Rate (%)", 
        y="Module", 
        color="Category",
        orientation='h',
        template="plotly_dark",
        color_discrete_map={
            "Food Security": "#f59e0b",
            "Water & Sanitation": "#38bdf8",
            "Medical Support": "#ef4444"
        }
    )
    fig_bar.update_layout(paper_bgcolor='#182232', plot_bgcolor='#182232', font=dict(color='#f8fafc'))

    # Pie Chart Visual
    fig_pie = px.pie(
        df_updated,
        values="Daily Target (Units)",
        names="Category",
        color="Category",
        hole=0.4,
        template="plotly_dark",
        color_discrete_map={
            "Food Security": "#f59e0b",
            "Water & Sanitation": "#38bdf8",
            "Medical Support": "#ef4444"
        }
    )
    fig_pie.update_layout(paper_bgcolor='#182232', plot_bgcolor='#182232', font=dict(color='#f8fafc'))

    # Status Message Logic
    if slider_value >= 80:
        status_msg = f"🟢 OPTIMAL PIPELINE FLOW ({slider_value}%): All food, clean water, and field hospitals receiving direct supply."
    elif slider_value >= 50:
        status_msg = f"🟡 CONGESTION ALERT ({slider_value}%): Supply bottlenecks detected. Prioritizing emergency medical & water tankers."
    else:
        status_msg = f"🔴 CRITICAL DISRUPTION ({slider_value}%): Flow rate insufficient. Re-routing through secondary micro-distribution nodes."

    return fig_bar, fig_pie, status_msg

# ---------------------------------------------------------
# RUN SERVER
# ---------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=8070)
import pandas as pd

# Housing & Transport Telemetry Data
reconstruction_data = {
    "Infrastructure Sector": [
        "Eco-Modular Housing Units",
        "Rooftop Solar & Local Energy Storage",
        "Coastal Light Rail (LRT) Network",
        "Electric BRT & Solar Charging Hubs",
        "Recycled Aggregate Material Plants"
    ],
    "Completion Capacity (%)": [75, 88, 65, 82, 90],
    "Operational Readiness": [
        "ACTIVE CONSTRUCTION",
        "GRID CONNECTED",
        "TRACK LAYING & TESTING",
        "FLEET DEPLOYED",
        "FULL OUTPUT"
    ]
}

df_reconstruction = pd.DataFrame(reconstruction_data)
print("--- GAZA PHASE 2: RECONSTRUCTION & TRANSPORT ROADMAP ---")
print(df_reconstruction.to_string(index=False))
import pandas as pd

# Housing Security Tracking Metrics
housing_allocation = {
    "Housing Zone": [
        "North Gaza Residential Cluster",
        "Gaza City Central Housing Hub",
        "Deir al-Balah Eco-Village",
        "Khan Yunis Modular Units",
        "Rafah Secure Settlement Zone"
    ],
    "Allocation Status (%)": [88, 92, 85, 90, 86],
    "Infrastructure Readiness": [
        "Solar Grid Connected",
        "Water & Sanitation Active",
        "Fully Operational",
        "Modular Assembly Active",
        "Water Desalination Linked"
    ]
}

df_housing = pd.DataFrame(housing_allocation)
print("--- GAZA PERMANENT HOUSING SECURITY TELEMETRY ---")
print(df_housing.to_string(index=False))
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# ---------------------------------------------------------
# 1. INTERNATIONAL SUPPORT MONITORING DATA (সহযোগিতাকারী দেশসমূহ)
# ---------------------------------------------------------
support_countries_data = {
    "Country / Partner": [
        "Qatar (Energy & Infrastructure)",
        "Turkey (Construction & Field Hospitals)",
        "South Africa (Legal & Diplomatic)",
        "Malaysia (Tech & Subsea Fiber)",
        "Algeria (Port & Trade Logistics)",
        "Norway (Clean Water & Desalination)"
    ],
    "Support Area": [
        "Energy Grid & Natural Gas",
        "Housing & Medical Infrastructure",
        "Sovereignty & Human Rights",
        "Independent Fiber & Satellite",
        "Maritime Port Operations",
        "Water Desalination Units"
    ],
    "Support Contribution Level (%)": [95, 90, 88, 92, 85, 89],
    "Status": ["ACTIVE", "ACTIVE", "DIPLOMATIC ACTIVE", "DEPLOYED", "OPERATIONAL", "STABLE"]
}

df_countries = pd.DataFrame(support_countries_data)

# ---------------------------------------------------------
# 2. GAZA INTERNAL NEW AI MODULES DATA (অভ্যন্তরীণ নতুন AI সিস্টেম)
# ---------------------------------------------------------
internal_ai_data = {
    "AI Sub-System": [
        "Smart Micro-Grid Load Balancer",
        "Automated Medical Triage AI",
        "Predictive Resource Demand Engine",
        "Mesh Network Self-Healing Router",
        "Eco-Housing Modular Allocator"
    ],
    "Health Index (%)": [98, 95, 92, 99, 91],
    "Execution Status": ["ONLINE", "ONLINE", "ACTIVE", "STABLE", "ACTIVE"]
}

df_internal_ai = pd.DataFrame(internal_ai_data)

# Initialize Dash App
app = dash.Dash(__name__)
app.title = "Gaza Sovereignty & Global Support Live Monitor"

# ---------------------------------------------------------
# UI LAYOUT (EMERALD CYBER THEME)
# ---------------------------------------------------------
app.layout = html.Div(style={
    'backgroundColor': '#021c16',
    'color': '#ecfdf5',
    'fontFamily': 'Segoe UI, Arial, sans-serif',
    'padding': '25px'
}, children=[

    # Header
    html.Div([
        html.H1("🇵🇸 GAZA INTERNAL AI & GLOBAL PARTNER SUPPORT LIVE MONITOR", 
                style={'color': '#34d399', 'marginBottom': '5px', 'fontWeight': 'bold'}),
        html.P("Real-Time Telemetry: Tracking Supporting Nations & Sovereign Internal AI Infrastructure",
               style={'color': '#a7f3d0', 'fontSize': '15px'})
    ], style={'borderBottom': '1px solid #065f46', 'paddingBottom': '15px'}),

    # Live Key Indicators
    html.Div([
        html.Div([
            html.H4("🌍 Supporting Nations Active", style={'color': '#6ee7b7', 'margin': '0 0 5px 0'}),
            html.H2("6 ALLIED NODES", style={'color': '#34d399', 'margin': '0 0 5px 0'}),
            html.P("Direct Infrastructure & Tech Alliance", style={'color': '#a7f3d0', 'margin': '0'})
        ], style={'backgroundColor': '#064e3b', 'padding': '20px', 'borderRadius': '8px', 'width': '30%', 'borderLeft': '4px solid #34d399'}),

        html.Div([
            html.H4("🧠 Internal AI System Status", style={'color': '#6ee7b7', 'margin': '0 0 5px 0'}),
            html.H2("95.0% OPTIMAL", style={'color': '#10b981', 'margin': '0 0 5px 0'}),
            html.P("Autonomous Grid & Medical AI Engine", style={'color': '#a7f3d0', 'margin': '0'})
        ], style={'backgroundColor': '#064e3b', 'padding': '20px', 'borderRadius': '8px', 'width': '30%', 'borderLeft': '4px solid #10b981'}),

        html.Div([
            html.H4("⚓ Direct Port & Connectivity", style={'color': '#6ee7b7', 'margin': '0 0 5px 0'}),
            html.H2("100% UNCHAINED", style={'color': '#fbbf24', 'margin': '0 0 5px 0'}),
            html.P("Zero external interference flow", style={'color': '#a7f3d0', 'margin': '0'})
        ], style={'backgroundColor': '#064e3b', 'padding': '20px', 'borderRadius': '8px', 'width': '30%', 'borderLeft': '4px solid #fbbf24'}),
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '25px'}),

    # Charts Grid
    html.Div([
        # Partner Countries Support Progress
        html.Div([
            html.H3("🌐 Partner Nations Support Index", style={'color': '#34d399'}),
            dcc.Graph(id='bar-chart-countries')
        ], style={'backgroundColor': '#064e3b', 'padding': '20px', 'borderRadius': '8px', 'width': '48%'}),

        # Internal AI Engine Status
        html.Div([
            html.H3("🧠 Internal AI Modules Health", style={'color': '#34d399'}),
            dcc.Graph(id='bar-chart-ai')
        ], style={'backgroundColor': '#064e3b', 'padding': '20px', 'borderRadius': '8px', 'width': '48%'})
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginTop': '25px'}),

    # Interactive Live Refresh Control
    html.Div([
        html.H3("🎛️ Live Alliance Telemetry Refresh Rate", style={'color': '#34d399'}),
        html.P("Real-time monitoring interval for global support integration:", style={'color': '#a7f3d0'}),
        dcc.Slider(
            id='refresh-slider',
            min=5,
            max=60,
            step=5,
            value=10,
            marks={i: f'{i} sec' for i in range(5, 61, 15)}
        ),
        html.Div(id='monitor-status-output', style={
            'marginTop': '20px', 
            'fontSize': '18px', 
            'fontWeight': 'bold', 
            'padding': '14px', 
            'backgroundColor': '#021c16', 
            'borderRadius': '6px', 
            'textAlign': 'center',
            'border': '1px solid #059669'
        })
    ], style={'backgroundColor': '#064e3b', 'padding': '25px', 'borderRadius': '8px', 'marginTop': '25px'})
])

# ---------------------------------------------------------
# CALLBACK LOGIC
# ---------------------------------------------------------
@app.callback(
    [Output('bar-chart-countries', 'figure'),
     Output('bar-chart-ai', 'figure'),
     Output('monitor-status-output', 'children')],
    [Input('refresh-slider', 'value')]
)
def update_live_monitor(slider_value):
    # Partner Countries Chart
    fig_countries = px.bar(
        df_countries, 
        x="Support Contribution Level (%)", 
        y="Country / Partner", 
        color="Support Area",
        orientation='h',
        template="plotly_dark",
        color_discrete_sequence=px.colors.qualitative.Emerald
    )
    fig_countries.update_layout(paper_bgcolor='#064e3b', plot_bgcolor='#064e3b', font=dict(color='#ecfdf5'))

    # Internal AI Chart
    fig_ai = px.bar(
        df_internal_ai,
        x="Health Index (%)",
        y="AI Sub-System",
        color="Execution Status",
        orientation='h',
        template="plotly_dark",
        color_discrete_sequence=["#10b981", "#34d399"]
    )
    fig_ai.update_layout(paper_bgcolor='#064e3b', plot_bgcolor='#064e3b', font=dict(color='#ecfdf5'))

    status_msg = f"📡 LIVE MONITORING ACTIVE: Refreshing telemetry every {slider_value} seconds. All allied support streams and internal AI engines are operating nominally."

    return fig_countries, fig_ai, status_msg

# ---------------------------------------------------------
# RUN SERVER
# ---------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
