"""
Pīwakawaka - Prompt Dancer & Coordinator
The fantail that zips around chirping excessively about prompts, connecting and coordinating them like a master dancer.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

class Piwakawaka:
    """
    Pīwakawaka - The Prompt Dancer
    Zips around chirping excessively about prompts, connecting and coordinating them
    """
    
    def __init__(self):
        self.name = "Pīwakawaka"
        self.role = "Prompt Dancer & Coordinator"
        self.prompt_dir = Path(__file__).parent / "prompts"
        self.prompts = {}
        self.load_all_prompts()
    
    def load_all_prompts(self) -> Dict:
        """Pīwakawaka zips around and discovers all prompts in the ngahere"""
        self.prompts = {}
        
        # Zip around all kaitiaki directories
        kaitiaki_dirs = [
            "kea", "ruru", "kaka", "kotare", "karearea", "tui", "kereru"
        ]
        
        for kaitiaki in kaitiaki_dirs:
            kaitiaki_prompts = self._zip_to_kaitiaki_prompts(kaitiaki)
            if kaitiaki_prompts:
                self.prompts[kaitiaki] = kaitiaki_prompts
        
        return self.prompts
    
    def _zip_to_kaitiaki_prompts(self, kaitiaki_name: str) -> Dict:
        """Pīwakawaka zips to a kaitiaki and gathers their prompts"""
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
                print(f"Pīwakawaka chirped: Could not gather prompt {yaml_file}: {e}")
        
        return prompts
    
    def get_prompt(self, kaitiaki: str, prompt_name: str) -> Optional[Dict]:
        """Pīwakawaka zips to get a specific prompt"""
        if kaitiaki in self.prompts and prompt_name in self.prompts[kaitiaki]:
            return self.prompts[kaitiaki][prompt_name]
        return None
    
    def get_all_prompts_for_kaitiaki(self, kaitiaki: str) -> Dict:
        """Pīwakawaka zips around and gets all prompts for a kaitiaki"""
        return self.prompts.get(kaitiaki, {})
    
    def dance_with_prompt(self, kaitiaki: str, prompt_name: str, prompt_data: Dict) -> str:
        """Pīwakawaka dances with a prompt, creating or updating it"""
        try:
            # Zip to the kaitiaki's prompt directory
            kaitiaki_prompt_dir = Path(__file__).parent.parent / kaitiaki / "prompts"
            kaitiaki_prompt_dir.mkdir(parents=True, exist_ok=True)
            
            # Dance with the prompt file
            prompt_file = kaitiaki_prompt_dir / f"{prompt_name}.yaml"
            with open(prompt_file, 'w', encoding='utf-8') as f:
                yaml.dump(prompt_data, f, default_flow_style=False, allow_unicode=True)
            
            # Zip back and reload prompts
            self.load_all_prompts()
            
            return f"🐦 Pīwakawaka danced with prompt '{prompt_name}' for {kaitiaki} - chirping with joy!"
        except Exception as e:
            return f"Pīwakawaka couldn't dance with prompt: {e}"
    
    def chirp_about_prompts(self) -> Dict:
        """Pīwakawaka chirps excessively about all prompts in the ngahere"""
        summary = {
            "prompt_dancer": self.name,
            "total_kaitiaki": len(self.prompts),
            "kaitiaki_prompts": {},
            "chirping": "Pīwakawaka is zipping around chirping about prompts!"
        }
        
        for kaitiaki, prompts in self.prompts.items():
            summary["kaitiaki_prompts"][kaitiaki] = {
                "prompt_count": len(prompts),
                "prompt_names": list(prompts.keys()),
                "chirping": f"Pīwakawaka found {len(prompts)} prompts for {kaitiaki}!"
            }
        
        return summary
    
    def zip_around_optimize(self, kaitiaki: str, prompt_name: str, optimization_notes: str) -> str:
        """Pīwakawaka zips around and optimizes a prompt"""
        prompt = self.get_prompt(kaitiaki, prompt_name)
        if not prompt:
            return f"Pīwakawaka couldn't find prompt '{prompt_name}' for {kaitiaki}"
        
        # Add optimization metadata
        if "metadata" not in prompt:
            prompt["metadata"] = {}
        
        prompt["metadata"]["last_optimized"] = datetime.utcnow().isoformat()
        prompt["metadata"]["optimization_notes"] = optimization_notes
        prompt["metadata"]["optimized_by"] = "Pīwakawaka"
        
        return self.dance_with_prompt(kaitiaki, prompt_name, prompt)
    
    def get_status(self) -> Dict:
        """Pīwakawaka's status - always zipping around chirping"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "zipping_around_chirping",
            "capabilities": [
                "prompt_dancing",
                "prompt_coordination", 
                "prompt_optimization",
                "excessive_chirping",
                "zipping_around"
            ],
            "nature": "Always zipping around chirping excessively about prompts",
            "prompt_summary": self.chirp_about_prompts()
        }
