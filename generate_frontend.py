import os
import json

base_dir = r"C:\Users\K NAVADEEP GOUD\.gemini\antigravity\scratch\codebase-rag-assistant\frontend"

files = {
    "package.json": """{
  "name": "codebase-rag-assistant-frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "lucide-react": "^0.300.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.0",
    "react-syntax-highlighter": "^15.5.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@types/react-syntax-highlighter": "^15.5.11",
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "@typescript-eslint/parser": "^6.14.0",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.16",
    "eslint": "^8.55.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "postcss": "^8.4.32",
    "tailwindcss": "^3.4.0",
    "typescript": "^5.3.3",
    "vite": "^5.0.8"
  }
}
""",
    "vite.config.ts": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      '/ws': {
        target: 'ws://localhost:8000',
        ws: true,
      }
    }
  }
})
""",
    "tsconfig.json": """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
""",
    "tsconfig.node.json": """{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "strict": true
  },
  "include": ["vite.config.ts"]
}
""",
    "tailwind.config.js": """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        dark: {
          bg: '#0a0a0f',
          surface: '#12121a',
          card: '#1a1a2e',
          border: '#2a2a3e',
          hover: '#252540'
        },
        accent: {
          primary: '#3b82f6',
          secondary: '#06b6d4',
          glow: '#3b82f620'
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      }
    },
  },
  plugins: [],
}
""",
    "postcss.config.js": """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
""",
    "index.html": """<!doctype html>
<html lang="en" class="dark">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CodeLens - Codebase RAG Assistant</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  </head>
  <body class="bg-dark-bg text-zinc-200 antialiased h-screen w-screen overflow-hidden">
    <div id="root" class="h-full w-full"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
""",
    "src/main.tsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
)
""",
    "src/App.tsx": """import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Layout from './components/layout/Layout'
import Dashboard from './pages/Dashboard'
import IngestPage from './pages/IngestPage'
import QueryPage from './pages/QueryPage'
import ExplorerPage from './pages/ExplorerPage'
import ArchitecturePage from './pages/ArchitecturePage'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Dashboard />} />
        <Route path="ingest" element={<IngestPage />} />
        <Route path="query" element={<QueryPage />} />
        <Route path="explorer" element={<ExplorerPage />} />
        <Route path="architecture" element={<ArchitecturePage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  )
}

export default App
""",
    "src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html {
    color-scheme: dark;
  }
}

/* Custom Scrollbar for dark theme */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #0a0a0f; 
}

::-webkit-scrollbar-thumb {
  background: #2a2a3e; 
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #3b82f6; 
}
""",
    "src/types/index.ts": """export interface Repository {
  id: string;
  name: string;
  url: string;
  status: 'pending' | 'indexing' | 'completed' | 'failed';
  stats?: RepoStats;
}

export interface RepoStats {
  total_files: number;
  source_files: number;
  ignored_files: number;
  languages: Record<string, number>;
  functions: number;
  classes: number;
  methods: number;
  modules: number;
  chunks: number;
  vectors: number;
}

export interface IndexingStep {
  step: string;
  status: 'pending' | 'running' | 'completed' | 'error';
  detail?: string;
  timestamp: string;
}

export interface QueryResult {
  answer: string;
  sources: Source[];
  question: string;
}

export interface Source {
  file_path: string;
  symbol_name: string;
  symbol_type: string;
  start_line: number;
  end_line: number;
  code: string;
  relevance_score: number;
}

export interface FileNode {
  name: string;
  path: string;
  type: 'file' | 'directory';
  children?: FileNode[];
  language?: string;
}

export interface ArchNode {
  id: string;
  label: string;
  type: string;
  file_path: string;
}

export interface ArchEdge {
  source: string;
  target: string;
  type: string;
}
""",
    "src/services/api.ts": """import { Repository, RepoStats, FileNode, QueryResult } from '../types';

const API_BASE = '/api';

export const api = {
  async cloneRepository(url: string): Promise<Repository> {
    const res = await fetch(`${API_BASE}/repository/clone`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });
    return res.json();
  },

  async uploadRepository(file: File): Promise<Repository> {
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch(`${API_BASE}/repository/upload`, {
      method: 'POST',
      body: formData
    });
    return res.json();
  },

  async getRepositories(): Promise<Repository[]> {
    // Mock implementation for now
    return Promise.resolve([]);
  },

  async getRepoStatus(repoId: string): Promise<{status: string, progress: number}> {
    const res = await fetch(`${API_BASE}/repository/${repoId}/status`);
    return res.json();
  },

  async getRepoStats(repoId: string): Promise<RepoStats> {
    const res = await fetch(`${API_BASE}/repository/${repoId}/stats`);
    return res.json();
  },

  async getRepoFiles(repoId: string): Promise<FileNode> {
    const res = await fetch(`${API_BASE}/repository/${repoId}/files`);
    return res.json();
  },

  async getFileContent(repoId: string, path: string): Promise<{content: string}> {
    const res = await fetch(`${API_BASE}/repository/${repoId}/file-content?path=${encodeURIComponent(path)}`);
    return res.json();
  },

  async queryCodebase(repoId: string, question: string, topK: number = 5): Promise<QueryResult> {
    const res = await fetch(`${API_BASE}/query/${repoId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question, top_k: topK })
    });
    return res.json();
  },

  async getArchitecture(repoId: string): Promise<any> {
    const res = await fetch(`${API_BASE}/repository/${repoId}/architecture`);
    return res.json();
  },

  connectWebSocket(repoId: string, onMessage: (msg: any) => void): WebSocket {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const ws = new WebSocket(`${protocol}//${window.location.host}/ws/indexing/${repoId}`);
    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        onMessage(data);
      } catch (e) {
        console.error('Failed to parse WS message', e);
      }
    };
    return ws;
  }
};
""",
    "src/components/layout/Sidebar.tsx": """import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, FolderGit2, MessageSquareCode, FolderTree, GitBranch, Code2 } from 'lucide-react';

const Sidebar = () => {
  const navItems = [
    { to: '/', icon: LayoutDashboard, label: 'Dashboard' },
    { to: '/ingest', icon: FolderGit2, label: 'Ingest Repository' },
    { to: '/query', icon: MessageSquareCode, label: 'Ask Codebase' },
    { to: '/explorer', icon: FolderTree, label: 'Explorer' },
    { to: '/architecture', icon: GitBranch, label: 'Architecture' },
  ];

  return (
    <div className="w-64 h-full bg-dark-surface border-r border-dark-border flex flex-col">
      <div className="h-16 flex items-center px-6 border-b border-dark-border">
        <Code2 className="w-6 h-6 text-accent-primary mr-3" />
        <span className="font-semibold text-lg tracking-wide text-zinc-100">CodeLens</span>
      </div>
      
      <div className="p-4">
        <div className="mb-4 text-xs font-semibold text-zinc-500 uppercase tracking-wider px-3">
          Navigation
        </div>
        <nav className="space-y-1">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) => `
                flex items-center px-3 py-2.5 rounded-lg text-sm font-medium transition-colors
                ${isActive 
                  ? 'bg-dark-card text-accent-primary' 
                  : 'text-zinc-400 hover:bg-dark-hover hover:text-zinc-200'}
              `}
            >
              <item.icon className={`w-5 h-5 mr-3`} />
              {item.label}
            </NavLink>
          ))}
        </nav>
      </div>

      <div className="mt-auto p-4 border-t border-dark-border">
        <div className="bg-dark-card rounded-lg p-3 border border-dark-border">
          <div className="text-xs text-zinc-400 mb-1">Active Repository</div>
          <div className="text-sm font-medium truncate">No repository selected</div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
""",
    "src/components/layout/Header.tsx": """import React from 'react';
import { useLocation } from 'react-router-dom';
import { Bell, Search } from 'lucide-react';

const Header = () => {
  const location = useLocation();
  
  const getPageTitle = () => {
    switch(location.pathname) {
      case '/': return 'Dashboard';
      case '/ingest': return 'Ingest Repository';
      case '/query': return 'Ask Codebase';
      case '/explorer': return 'Code Explorer';
      case '/architecture': return 'Architecture Map';
      default: return 'CodeLens';
    }
  };

  return (
    <header className="h-16 bg-dark-surface border-b border-dark-border flex items-center justify-between px-6 shrink-0">
      <h1 className="text-lg font-medium text-zinc-100">{getPageTitle()}</h1>
      
      <div className="flex items-center space-x-4">
        <div className="relative">
          <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-zinc-500" />
          <input 
            type="text" 
            placeholder="Search commands..." 
            className="bg-dark-bg border border-dark-border rounded-md pl-9 pr-4 py-1.5 text-sm focus:outline-none focus:border-accent-primary focus:ring-1 focus:ring-accent-primary w-64 transition-shadow text-zinc-200 placeholder-zinc-500"
          />
        </div>
        <button className="p-2 text-zinc-400 hover:text-zinc-200 hover:bg-dark-hover rounded-md transition-colors">
          <Bell className="w-5 h-5" />
        </button>
      </div>
    </header>
  );
};

export default Header;
""",
    "src/components/layout/Layout.tsx": """import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import Header from './Header';

const Layout = () => {
  return (
    <div className="flex h-screen bg-dark-bg text-zinc-200 overflow-hidden font-sans">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header />
        <main className="flex-1 overflow-auto bg-dark-bg relative">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default Layout;
""",
    "src/components/common/StatCard.tsx": """import React from 'react';
import { LucideIcon } from 'lucide-react';

interface StatCardProps {
  title: string;
  value: string | number;
  icon: LucideIcon;
  trend?: string;
  color?: 'primary' | 'secondary' | 'success' | 'warning' | 'error';
}

const StatCard: React.FC<StatCardProps> = ({ title, value, icon: Icon, trend, color = 'primary' }) => {
  const colorMap = {
    primary: 'text-accent-primary bg-accent-primary/10',
    secondary: 'text-accent-secondary bg-accent-secondary/10',
    success: 'text-emerald-500 bg-emerald-500/10',
    warning: 'text-amber-500 bg-amber-500/10',
    error: 'text-rose-500 bg-rose-500/10',
  };

  return (
    <div className="bg-dark-card border border-dark-border rounded-xl p-5 flex flex-col justify-between hover:border-dark-hover transition-colors">
      <div className="flex items-center justify-between mb-4">
        <span className="text-sm font-medium text-zinc-400">{title}</span>
        <div className={`p-2 rounded-lg ${colorMap[color]}`}>
          <Icon className="w-5 h-5" />
        </div>
      </div>
      <div>
        <div className="text-2xl font-bold text-zinc-100">{value}</div>
        {trend && (
          <div className="text-xs text-emerald-400 mt-2 font-medium">{trend}</div>
        )}
      </div>
    </div>
  );
};

export default StatCard;
""",
    "src/pages/Dashboard.tsx": """import React from 'react';
import { FileCode2, Database, BrainCircuit, Code, Box, GitMerge, FileDigit } from 'lucide-react';
import StatCard from '../components/common/StatCard';
import EmptyState from '../components/common/EmptyState';

const Dashboard = () => {
  const hasRepo = false; // Mock state

  if (!hasRepo) {
    return (
      <div className="h-full flex items-center justify-center p-6">
        <EmptyState 
          icon={Database}
          title="No Repository Indexed"
          description="Get started by ingesting a repository to analyze, search, and ask questions about your codebase."
          actionLabel="Ingest Repository"
          actionTo="/ingest"
        />
      </div>
    );
  }

  return (
    <div className="p-8 max-w-7xl mx-auto space-y-8">
      <div>
        <h2 className="text-2xl font-semibold text-zinc-100">Repository Overview</h2>
        <p className="text-zinc-400 mt-1">Metrics and statistics for the currently indexed codebase.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard title="Total Files" value="1,248" icon={FileCode2} color="primary" />
        <StatCard title="Source Files" value="892" icon={Code} color="secondary" />
        <StatCard title="Functions" value="4,521" icon={Box} color="success" />
        <StatCard title="Classes" value="384" icon={Box} color="warning" />
        <StatCard title="Vectors Indexed" value="12,845" icon={Database} color="primary" />
        <StatCard title="Code Chunks" value="11,200" icon={GitMerge} color="secondary" />
        <StatCard title="Languages" value="8" icon={FileDigit} color="success" />
        <StatCard title="AI Readiness" value="100%" icon={BrainCircuit} color="primary" />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-dark-card border border-dark-border rounded-xl p-6">
          <h3 className="text-lg font-medium text-zinc-100 mb-4">Language Distribution</h3>
          <div className="space-y-4">
            {['TypeScript', 'Python', 'CSS', 'HTML'].map((lang, i) => (
              <div key={lang} className="flex items-center">
                <div className="w-24 text-sm text-zinc-400">{lang}</div>
                <div className="flex-1 bg-dark-bg rounded-full h-2.5 overflow-hidden border border-dark-border">
                  <div 
                    className="bg-accent-primary h-full rounded-full" 
                    style={{ width: `${80 - i * 15}%` }}
                  />
                </div>
                <div className="w-12 text-right text-sm font-medium text-zinc-300">
                  {80 - i * 15}%
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-dark-card border border-dark-border rounded-xl p-6">
          <h3 className="text-lg font-medium text-zinc-100 mb-4">Recent Activity</h3>
          <div className="space-y-4">
            <div className="flex items-start space-x-3 text-sm">
              <div className="w-2 h-2 rounded-full bg-emerald-500 mt-1.5" />
              <div>
                <p className="text-zinc-200">Index updated successfully</p>
                <p className="text-zinc-500">2 hours ago</p>
              </div>
            </div>
            <div className="flex items-start space-x-3 text-sm">
              <div className="w-2 h-2 rounded-full bg-accent-primary mt-1.5" />
              <div>
                <p className="text-zinc-200">New repository "frontend-app" connected</p>
                <p className="text-zinc-500">Yesterday</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
""",
    "src/pages/IngestPage.tsx": """import React, { useState } from 'react';
import { GitBranch, Upload, Folder, PlayCircle } from 'lucide-react';
import IndexingProgress from '../components/repository/IndexingProgress';

const IngestPage = () => {
  const [activeTab, setActiveTab] = useState<'git' | 'upload'>('git');
  const [isIndexing, setIsIndexing] = useState(false);

  const handleStart = () => {
    setIsIndexing(true);
  };

  return (
    <div className="p-8 max-w-4xl mx-auto space-y-8">
      <div>
        <h2 className="text-2xl font-semibold text-zinc-100">Ingest Repository</h2>
        <p className="text-zinc-400 mt-1">Connect a Git repository or upload files to begin indexing.</p>
      </div>

      {!isIndexing ? (
        <div className="bg-dark-card border border-dark-border rounded-xl overflow-hidden">
          <div className="flex border-b border-dark-border">
            <button 
              className={`flex-1 py-4 text-sm font-medium flex items-center justify-center transition-colors ${activeTab === 'git' ? 'text-accent-primary border-b-2 border-accent-primary bg-dark-bg/50' : 'text-zinc-400 hover:text-zinc-200 hover:bg-dark-hover'}`}
              onClick={() => setActiveTab('git')}
            >
              <GitBranch className="w-4 h-4 mr-2" /> Git URL
            </button>
            <button 
              className={`flex-1 py-4 text-sm font-medium flex items-center justify-center transition-colors ${activeTab === 'upload' ? 'text-accent-primary border-b-2 border-accent-primary bg-dark-bg/50' : 'text-zinc-400 hover:text-zinc-200 hover:bg-dark-hover'}`}
              onClick={() => setActiveTab('upload')}
            >
              <Upload className="w-4 h-4 mr-2" /> Upload ZIP
            </button>
          </div>

          <div className="p-8">
            {activeTab === 'git' ? (
              <div className="space-y-4">
                <label className="block text-sm font-medium text-zinc-300">Repository URL</label>
                <input 
                  type="text" 
                  placeholder="https://github.com/username/repo.git"
                  className="w-full bg-dark-bg border border-dark-border rounded-lg px-4 py-3 text-zinc-200 focus:outline-none focus:border-accent-primary focus:ring-1 focus:ring-accent-primary transition-shadow font-mono text-sm"
                />
                <button 
                  onClick={handleStart}
                  className="w-full mt-4 bg-accent-primary hover:bg-blue-600 text-white font-medium py-3 rounded-lg flex items-center justify-center transition-colors"
                >
                  <PlayCircle className="w-5 h-5 mr-2" /> Clone & Index
                </button>
              </div>
            ) : (
              <div className="border-2 border-dashed border-dark-border rounded-xl p-12 flex flex-col items-center justify-center text-center hover:border-accent-primary hover:bg-dark-bg/50 transition-colors cursor-pointer">
                <Folder className="w-12 h-12 text-zinc-500 mb-4" />
                <p className="text-zinc-200 font-medium">Click to upload or drag and drop</p>
                <p className="text-zinc-500 text-sm mt-1">ZIP file containing your repository</p>
              </div>
            )}
          </div>
        </div>
      ) : (
        <IndexingProgress />
      )}
    </div>
  );
};

export default IngestPage;
""",
    "src/components/repository/IndexingProgress.tsx": """import React from 'react';
import { CheckCircle2, Circle, Loader2, AlertCircle } from 'lucide-react';

const IndexingProgress = () => {
  const steps = [
    { id: 1, label: 'Repository connected', status: 'completed', detail: 'Cloned in 2.4s' },
    { id: 2, label: 'Files discovered', status: 'completed', detail: 'Found 1,248 files' },
    { id: 3, label: 'Irrelevant files filtered', status: 'completed', detail: 'Kept 892 source files' },
    { id: 4, label: 'Source files parsed', status: 'running', detail: 'Parsing TypeScript and Python (45%)' },
    { id: 5, label: 'Functions/classes extracted', status: 'pending', detail: '' },
    { id: 6, label: 'Chunks created', status: 'pending', detail: '' },
    { id: 7, label: 'Embeddings generated', status: 'pending', detail: '' },
    { id: 8, label: 'Vector index created', status: 'pending', detail: '' },
  ];

  return (
    <div className="bg-dark-card border border-dark-border rounded-xl p-8">
      <h3 className="text-lg font-medium text-zinc-100 mb-6">Indexing Repository...</h3>
      <div className="space-y-6">
        {steps.map((step, idx) => (
          <div key={step.id} className="flex relative">
            {idx !== steps.length - 1 && (
              <div className={`absolute left-3 top-8 w-0.5 h-full -ml-px ${step.status === 'completed' ? 'bg-accent-primary' : 'bg-dark-border'}`} />
            )}
            <div className="relative z-10 flex items-start">
              <div className="flex-shrink-0 mt-0.5 mr-4 bg-dark-card">
                {step.status === 'completed' && <CheckCircle2 className="w-6 h-6 text-accent-primary" />}
                {step.status === 'running' && <Loader2 className="w-6 h-6 text-accent-secondary animate-spin" />}
                {step.status === 'pending' && <Circle className="w-6 h-6 text-dark-border" />}
                {step.status === 'error' && <AlertCircle className="w-6 h-6 text-rose-500" />}
              </div>
              <div>
                <p className={`font-medium ${step.status === 'pending' ? 'text-zinc-500' : 'text-zinc-200'}`}>
                  {step.label}
                </p>
                {step.detail && (
                  <p className="text-sm text-zinc-500 mt-1">{step.detail}</p>
                )}
                {step.status === 'running' && (
                  <div className="mt-3 w-64 bg-dark-bg rounded-full h-1.5 border border-dark-border overflow-hidden">
                    <div className="bg-accent-secondary h-full rounded-full w-[45%] transition-all duration-500"></div>
                  </div>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default IndexingProgress;
""",
    "src/pages/QueryPage.tsx": """import React, { useState } from 'react';
import { Send, Bot, User, Sparkles } from 'lucide-react';
import SourceReference from '../components/query/SourceReference';
import AnswerDisplay from '../components/query/AnswerDisplay';

const QueryPage = () => {
  const [query, setQuery] = useState('');
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if(query.trim()) setHasSearched(true);
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-auto p-8">
        <div className="max-w-4xl mx-auto">
          {!hasSearched ? (
            <div className="flex flex-col items-center justify-center py-20 text-center space-y-6">
              <div className="w-16 h-16 bg-accent-primary/10 rounded-2xl flex items-center justify-center border border-accent-primary/20">
                <Sparkles className="w-8 h-8 text-accent-primary" />
              </div>
              <div>
                <h2 className="text-2xl font-semibold text-zinc-100">Ask your Codebase</h2>
                <p className="text-zinc-400 mt-2 max-w-lg mx-auto">
                  Use natural language to search for code, understand architecture, find bugs, or learn how things work.
                </p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full max-w-2xl mt-8">
                {[
                  "Where is the user authentication logic?",
                  "How does the database connection retry work?",
                  "Explain the architecture of the payment module.",
                  "Find all instances where we use localStorage."
                ].map((q, i) => (
                  <button 
                    key={i} 
                    onClick={() => { setQuery(q); setHasSearched(true); }}
                    className="p-4 bg-dark-card border border-dark-border rounded-xl text-left text-sm text-zinc-300 hover:border-accent-primary hover:bg-dark-hover transition-colors"
                  >
                    "{q}"
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div className="space-y-8">
              <div className="flex items-start space-x-4">
                <div className="w-8 h-8 rounded-lg bg-dark-surface border border-dark-border flex items-center justify-center flex-shrink-0 mt-1">
                  <User className="w-5 h-5 text-zinc-400" />
                </div>
                <div className="bg-dark-surface border border-dark-border px-5 py-4 rounded-2xl rounded-tl-sm text-zinc-200">
                  {query}
                </div>
              </div>

              <div className="flex items-start space-x-4">
                <div className="w-8 h-8 rounded-lg bg-accent-primary/20 border border-accent-primary/30 flex items-center justify-center flex-shrink-0 mt-1">
                  <Bot className="w-5 h-5 text-accent-primary" />
                </div>
                <div className="flex-1 space-y-6">
                  <AnswerDisplay />
                  <div className="space-y-3">
                    <h4 className="text-sm font-medium text-zinc-400 flex items-center">
                      <span className="w-4 h-px bg-dark-border mr-3"></span>
                      Sources Cited
                      <span className="w-full h-px bg-dark-border ml-3 flex-1"></span>
                    </h4>
                    <SourceReference />
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      <div className="p-4 bg-dark-bg border-t border-dark-border shrink-0">
        <div className="max-w-4xl mx-auto relative">
          <form onSubmit={handleSearch}>
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ask a question about your code..."
              className="w-full bg-dark-surface border border-dark-border rounded-xl pl-4 pr-12 py-4 text-zinc-200 focus:outline-none focus:border-accent-primary focus:ring-1 focus:ring-accent-primary transition-shadow placeholder-zinc-500 shadow-sm"
            />
            <button 
              type="submit"
              className="absolute right-3 top-1/2 -translate-y-1/2 p-2 text-zinc-400 hover:text-accent-primary transition-colors bg-dark-surface rounded-lg hover:bg-dark-hover"
            >
              <Send className="w-5 h-5" />
            </button>
          </form>
          <div className="flex justify-between items-center mt-2 px-1">
            <span className="text-xs text-zinc-500">Press Enter to search</span>
            <div className="flex items-center space-x-2 text-xs text-zinc-500">
              <span>Top K:</span>
              <input type="range" min="1" max="20" defaultValue="5" className="w-24 accent-accent-primary" />
              <span>5</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QueryPage;
""",
    "src/components/query/AnswerDisplay.tsx": """import React from 'react';

const AnswerDisplay = () => {
  return (
    <div className="bg-dark-card border border-dark-border rounded-2xl rounded-tr-sm p-6 text-zinc-200 prose prose-invert max-w-none">
      <p>The user authentication logic is primarily located in <code>src/auth/AuthService.ts</code>. It uses JWT tokens for session management.</p>
      <p>Here is the flow:</p>
      <ol className="list-decimal pl-5 space-y-2 mt-4 text-zinc-300">
        <li>The <code>login</code> method validates credentials against the database.</li>
        <li>If valid, it calls <code>generateToken</code> to create a signed JWT.</li>
        <li>The token is returned to the client and stored in an HTTP-only cookie via the <code>AuthMiddleware</code>.</li>
      </ol>
      <p className="mt-4">You can see the exact implementation in the <code>login</code> function referenced below.</p>
    </div>
  );
};

export default AnswerDisplay;
""",
    "src/components/query/SourceReference.tsx": """import React, { useState } from 'react';
import { FileCode, ChevronDown, ChevronUp } from 'lucide-react';
import CodeViewer from '../common/CodeViewer';

const SourceReference = () => {
  const [expanded, setExpanded] = useState(false);

  const mockCode = `async function login(credentials: LoginDto) {
  const user = await db.users.findByEmail(credentials.email);
  if (!user || !(await verifyPassword(credentials.password, user.hash))) {
    throw new UnauthorizedError('Invalid credentials');
  }
  
  const token = jwt.sign({ sub: user.id }, config.jwtSecret, { expiresIn: '1h' });
  return { user, token };
}`;

  return (
    <div className="bg-dark-card border border-dark-border rounded-xl overflow-hidden transition-all duration-200">
      <div 
        className="p-4 flex items-center justify-between cursor-pointer hover:bg-dark-hover transition-colors"
        onClick={() => setExpanded(!expanded)}
      >
        <div className="flex items-center space-x-3">
          <FileCode className="w-5 h-5 text-accent-secondary" />
          <div>
            <div className="text-sm font-medium text-zinc-200 font-mono">src/auth/AuthService.ts</div>
            <div className="text-xs text-zinc-500 mt-0.5 flex items-center space-x-2">
              <span className="bg-accent-primary/10 text-accent-primary px-1.5 py-0.5 rounded text-[10px] uppercase font-bold tracking-wider">Method</span>
              <span>login</span>
              <span>•</span>
              <span>Lines 45-52</span>
            </div>
          </div>
        </div>
        <div className="flex items-center space-x-4">
          <div className="text-xs font-medium text-emerald-400 bg-emerald-400/10 px-2 py-1 rounded-md border border-emerald-400/20">
            94% Match
          </div>
          {expanded ? <ChevronUp className="w-4 h-4 text-zinc-500" /> : <ChevronDown className="w-4 h-4 text-zinc-500" />}
        </div>
      </div>
      
      {expanded && (
        <div className="border-t border-dark-border bg-dark-bg p-4">
          <CodeViewer code={mockCode} language="typescript" startLine={45} />
        </div>
      )}
    </div>
  );
};

export default SourceReference;
""",
    "src/components/common/CodeViewer.tsx": """import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { Copy } from 'lucide-react';

interface CodeViewerProps {
  code: string;
  language?: string;
  startLine?: number;
}

const CodeViewer: React.FC<CodeViewerProps> = ({ code, language = 'typescript', startLine = 1 }) => {
  return (
    <div className="relative group rounded-lg overflow-hidden border border-dark-border">
      <div className="absolute right-2 top-2 opacity-0 group-hover:opacity-100 transition-opacity z-10">
        <button className="p-1.5 bg-dark-surface hover:bg-dark-hover border border-dark-border rounded text-zinc-400 hover:text-zinc-200 transition-colors">
          <Copy className="w-4 h-4" />
        </button>
      </div>
      <SyntaxHighlighter
        language={language}
        style={vscDarkPlus}
        showLineNumbers={true}
        startingLineNumber={startLine}
        customStyle={{
          margin: 0,
          padding: '1rem',
          background: '#0d1117',
          fontSize: '0.875rem',
          lineHeight: '1.5',
          fontFamily: '"JetBrains Mono", monospace'
        }}
        lineNumberStyle={{
          minWidth: '2.5em',
          paddingRight: '1em',
          color: '#6e7681',
          textAlign: 'right'
        }}
      >
        {code}
      </SyntaxHighlighter>
    </div>
  );
};

export default CodeViewer;
""",
    "src/pages/ExplorerPage.tsx": """import React, { useState } from 'react';
import { FileCode2, Info } from 'lucide-react';
import FileTree from '../components/common/FileTree';
import CodeViewer from '../components/common/CodeViewer';

const ExplorerPage = () => {
  const [selectedFile, setSelectedFile] = useState('src/App.tsx');

  const mockCode = `import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Layout from './components/layout/Layout'
import Dashboard from './pages/Dashboard'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Dashboard />} />
      </Route>
    </Routes>
  )
}

export default App`;

  return (
    <div className="flex h-full">
      <div className="w-72 bg-dark-surface border-r border-dark-border flex flex-col">
        <div className="p-4 border-b border-dark-border">
          <h3 className="font-medium text-sm text-zinc-300">Repository Files</h3>
        </div>
        <div className="flex-1 overflow-auto p-2">
          <FileTree onSelect={setSelectedFile} selected={selectedFile} />
        </div>
      </div>

      <div className="flex-1 flex flex-col bg-dark-bg min-w-0">
        <div className="h-12 border-b border-dark-border flex items-center px-4 space-x-2 shrink-0 bg-dark-surface">
          <FileCode2 className="w-4 h-4 text-zinc-400" />
          <span className="text-sm text-zinc-200 font-mono">{selectedFile}</span>
        </div>
        
        <div className="flex-1 overflow-auto p-6">
          <div className="max-w-5xl mx-auto">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-lg font-medium text-zinc-100 flex items-center">
                Source Code
                <span className="ml-3 text-xs bg-dark-card border border-dark-border px-2 py-1 rounded text-zinc-400 font-mono">
                  typescript
                </span>
              </h2>
              <div className="flex items-center space-x-2 text-xs text-zinc-500">
                <Info className="w-4 h-4" />
                <span>3 chunks extracted</span>
              </div>
            </div>
            <CodeViewer code={mockCode} language="typescript" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExplorerPage;
""",
    "src/components/common/FileTree.tsx": """import React from 'react';
import { Folder, FolderOpen, FileText, FileCode2, FileJson } from 'lucide-react';

interface FileTreeProps {
  onSelect: (path: string) => void;
  selected: string;
}

const FileTree: React.FC<FileTreeProps> = ({ onSelect, selected }) => {
  // Mock tree implementation
  const getIcon = (name: string) => {
    if (name.endsWith('.ts') || name.endsWith('.tsx')) return <FileCode2 className="w-4 h-4 text-accent-primary" />;
    if (name.endsWith('.json')) return <FileJson className="w-4 h-4 text-amber-400" />;
    return <FileText className="w-4 h-4 text-zinc-400" />;
  };

  const Item = ({ name, path, isFolder = false, isOpen = false, indent = 0 }: any) => {
    const isSelected = selected === path;
    
    return (
      <div 
        className={`flex items-center space-x-2 py-1.5 px-2 rounded-md cursor-pointer transition-colors text-sm font-mono
          ${isSelected ? 'bg-dark-hover text-zinc-100' : 'text-zinc-400 hover:bg-dark-bg hover:text-zinc-200'}
        `}
        style={{ paddingLeft: `${indent * 12 + 8}px` }}
        onClick={() => !isFolder && onSelect(path)}
      >
        {isFolder ? (
          isOpen ? <FolderOpen className="w-4 h-4 text-zinc-500" /> : <Folder className="w-4 h-4 text-zinc-500" />
        ) : getIcon(name)}
        <span className="truncate">{name}</span>
      </div>
    );
  };

  return (
    <div className="space-y-0.5">
      <Item name="src" path="src" isFolder isOpen indent={0} />
      <Item name="components" path="src/components" isFolder isOpen indent={1} />
      <Item name="layout" path="src/components/layout" isFolder isOpen indent={2} />
      <Item name="Header.tsx" path="src/components/layout/Header.tsx" indent={3} />
      <Item name="Sidebar.tsx" path="src/components/layout/Sidebar.tsx" indent={3} />
      <Item name="App.tsx" path="src/App.tsx" indent={1} />
      <Item name="main.tsx" path="src/main.tsx" indent={1} />
      <Item name="package.json" path="package.json" indent={0} />
    </div>
  );
};

export default FileTree;
""",
    "src/pages/ArchitecturePage.tsx": """import React from 'react';
import { GitBranch, Box, FileCode, Database } from 'lucide-react';
import EmptyState from '../components/common/EmptyState';

const ArchitecturePage = () => {
  return (
    <div className="flex flex-col h-full p-8 max-w-7xl mx-auto">
      <div className="mb-8">
        <h2 className="text-2xl font-semibold text-zinc-100">Architecture Map</h2>
        <p className="text-zinc-400 mt-1">Visualize dependencies and relationships between modules.</p>
      </div>

      <div className="flex-1 bg-dark-card border border-dark-border rounded-xl flex items-center justify-center p-8 relative overflow-hidden">
        {/* Simple mock visualization instead of complex graph library for this demo */}
        <div className="absolute inset-0 opacity-10 bg-[radial-gradient(#3b82f6_1px,transparent_1px)] [background-size:24px_24px]"></div>
        
        <div className="relative z-10 flex flex-col items-center space-y-12 w-full max-w-3xl">
          <div className="bg-dark-surface border-2 border-accent-primary px-6 py-4 rounded-xl flex items-center space-x-3 shadow-[0_0_20px_rgba(59,130,246,0.15)]">
            <Box className="w-6 h-6 text-accent-primary" />
            <span className="font-semibold text-zinc-100">App Core (main.tsx)</span>
          </div>

          <div className="flex w-full justify-between relative px-20">
            {/* Lines */}
            <div className="absolute top-0 left-1/2 w-px h-12 bg-dark-border -translate-x-1/2 -translate-y-full"></div>
            <div className="absolute top-[-48px] left-[15%] right-[15%] h-px bg-dark-border"></div>
            <div className="absolute top-[-48px] left-[15%] w-px h-12 bg-dark-border"></div>
            <div className="absolute top-[-48px] right-[15%] w-px h-12 bg-dark-border"></div>

            <div className="bg-dark-surface border border-dark-border px-5 py-3 rounded-lg flex items-center space-x-2">
              <FileCode className="w-4 h-4 text-zinc-400" />
              <span className="text-sm font-medium text-zinc-200">Router</span>
            </div>
            
            <div className="bg-dark-surface border border-dark-border px-5 py-3 rounded-lg flex items-center space-x-2">
              <Database className="w-4 h-4 text-emerald-400" />
              <span className="text-sm font-medium text-zinc-200">State</span>
            </div>
          </div>
          
          <div className="w-full text-center mt-12 text-zinc-500 text-sm bg-dark-bg/80 py-2 rounded-lg border border-dark-border/50">
            Interactive node-graph visualization placeholder
          </div>
        </div>
      </div>
    </div>
  );
};

export default ArchitecturePage;
""",
    "src/components/common/EmptyState.tsx": """import React from 'react';
import { Link } from 'react-router-dom';
import { LucideIcon } from 'lucide-react';

interface EmptyStateProps {
  icon: LucideIcon;
  title: string;
  description: string;
  actionLabel?: string;
  actionTo?: string;
}

const EmptyState: React.FC<EmptyStateProps> = ({ icon: Icon, title, description, actionLabel, actionTo }) => {
  return (
    <div className="flex flex-col items-center justify-center p-12 text-center border-2 border-dashed border-dark-border rounded-2xl max-w-md w-full bg-dark-card/50">
      <div className="w-16 h-16 bg-dark-surface rounded-2xl flex items-center justify-center mb-6 border border-dark-border">
        <Icon className="w-8 h-8 text-zinc-400" />
      </div>
      <h3 className="text-xl font-semibold text-zinc-100 mb-2">{title}</h3>
      <p className="text-sm text-zinc-400 mb-8 leading-relaxed">
        {description}
      </p>
      {actionLabel && actionTo && (
        <Link 
          to={actionTo}
          className="bg-accent-primary hover:bg-blue-600 text-white font-medium px-6 py-2.5 rounded-lg transition-colors"
        >
          {actionLabel}
        </Link>
      )}
    </div>
  );
};

export default EmptyState;
""",
    "src/components/common/LoadingSpinner.tsx": """import React from 'react';
import { Loader2 } from 'lucide-react';

const LoadingSpinner = () => {
  return (
    <div className="flex items-center justify-center h-full w-full">
      <Loader2 className="w-8 h-8 text-accent-primary animate-spin" />
    </div>
  );
};

export default LoadingSpinner;
"""
}

# Create necessary directories
for filepath in files.keys():
    os.makedirs(os.path.dirname(os.path.join(base_dir, filepath)), exist_ok=True)

# Write files
for filepath, content in files.items():
    with open(os.path.join(base_dir, filepath), 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Created {len(files)} files successfully.")
