"""
Kākā Prompt Hub - Central Prompt Coordinator and Carver
Kākā manages all prompts for the ngahere, carving and coordinating them like a master craftsman.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

class PromptHub:
    """
    Kākā's Prompt Hub - Central repository for all ngahere prompts
    Kākā carves, manages, and coordinates all prompts like a master craftsman
    """
    
    def __init__(self):
        self.name = "Kākā Prompt Hub"
        self.prompt_dir = Path(__file__).parent / "prompts"
        self.prompts = {}
        self.load_all_prompts()
    
    def load_all_prompts(self) -> Dict:
        """Load all prompts from the ngahere"""
        self.prompts = {}
        
        # Load prompts from all kaitiaki directories
        kaitiaki_dirs = [
            "kea", "ruru", "kaka", "kotare", "karearea", "tui", "kereru"
        ]
        
        for kaitiaki in kaitiaki_dirs:
            kaitiaki_prompts = self._load_kaitiaki_prompts(kaitiaki)
            if kaitiaki_prompts:
                self.prompts[kaitiaki] = kaitiaki_prompts
        
        return self.prompts
    
    def _load_kaitiaki_prompts(self, kaitiaki_name: str) -> Dict:
        """Load prompts for a specific kaitiaki"""
        kaitiaki_prompt_dir = Path(__file__).parent.parent / kaitiaki_name / "prompts"
        
        if not kaitiaki_prompt_dir.exists():
            return {}
        
        prompts = {}
        for yaml_file in kaitiaki_prompt_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    prompt_data = yaml.safe_load(f)
                    prompts[yaml_file.stem] = prompt_data
            except Exception as e:
                print(f"Warning: Could not load prompt {yaml_file}: {e}")
        
        return prompts
    
    def get_prompt(self, kaitiaki: str, prompt_name: str) -> Optional[Dict]:
        """Get a specific prompt for a kaitiaki"""
        if kaitiaki in self.prompts and prompt_name in self.prompts[kaitiaki]:
            return self.prompts[kaitiaki][prompt_name]
        return None
    
    def get_all_prompts_for_kaitiaki(self, kaitiaki: str) -> Dict:
        """Get all prompts for a specific kaitiaki"""
        return self.prompts.get(kaitiaki, {})
    
    def carve_new_prompt(self, kaitiaki: str, prompt_name: str, prompt_data: Dict) -> bool:
        """Kākā carves a new prompt into the ngahere"""
        try:
            # Ensure kaitiaki prompt directory exists
            kaitiaki_prompt_dir = Path(__file__).parent.parent / kaitiaki / "prompts"
            kaitiaki_prompt_dir.mkdir(parents=True, exist_ok=True)
            
            # Save the prompt
            prompt_file = kaitiaki_prompt_dir / f"{prompt_name}.yaml"
            with open(prompt_file, 'w', encoding='utf-8') as f:
                yaml.dump(prompt_data, f, default_flow_style=False, allow_unicode=True)
            
            # Reload prompts
            self.load_all_prompts()
            
            return True
        except Exception as e:
            print(f"Kākā couldn't carve prompt: {e}")
            return False
    
    def get_prompt_summary(self) -> Dict:
        """Get a summary of all prompts in the ngahere"""
        summary = {
            "prompt_hub": self.name,
            "total_kaitiaki": len(self.prompts),
            "kaitiaki_prompts": {}
        }
        
        for kaitiaki, prompts in self.prompts.items():
            summary["kaitiaki_prompts"][kaitiaki] = {
                "prompt_count": len(prompts),
                "prompt_names": list(prompts.keys())
            }
        
        return summary
    
    def optimize_prompt(self, kaitiaki: str, prompt_name: str, optimization_notes: str) -> bool:
        """Kākā optimizes an existing prompt"""
        prompt = self.get_prompt(kaitiaki, prompt_name)
        if not prompt:
            return False
        
        # Add optimization metadata
        if "metadata" not in prompt:
            prompt["metadata"] = {}
        
        prompt["metadata"]["last_optimized"] = datetime.utcnow().isoformat()
        prompt["metadata"]["optimization_notes"] = optimization_notes
        
        return self.carve_new_prompt(kaitiaki, prompt_name, prompt)
    
    def get_status(self) -> Dict:
        """Get Kākā's prompt hub status"""
        return {
            "kaitiaki": "Kākā",
            "role": "Prompt Carver & Coordinator",
            "status": "active",
            "prompt_hub": self.name,
            "capabilities": [
                "prompt_carving",
                "prompt_coordination", 
                "prompt_optimization",
                "central_prompt_management"
            ],
            "prompt_summary": self.get_prompt_summary()
        }

# Global prompt hub instance
prompt_hub = PromptHub()
