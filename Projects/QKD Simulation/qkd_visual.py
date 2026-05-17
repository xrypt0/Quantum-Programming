import sys
sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from qkd_simulation import simulate_qkd

num_bits = 10
eve_active = False

alice_bits, alice_bases, eve_bases, eve_bits, bob_bases, bob_bits, matching_indices, shared_key_alice, shared_key_bob = simulate_qkd(num_bits, eve_active)

fig = plt.figure(figsize=(15, 9))
fig.canvas.manager.set_window_title("BB84 QKD Simulation with Eavesdropper (Eve)")
plt.subplots_adjust(bottom=0.25, top=0.9, left=0.08, right=0.92)

ax_grid = fig.add_subplot(1, 2, 1)
ax_vector = fig.add_subplot(1, 2, 2)

slider_ax = plt.axes([0.1, 0.1, 0.4, 0.04])
bit_slider = Slider(slider_ax, 'Inspect Bit ', 0, num_bits - 1, valinit=0, valfmt='%0.0f', color='#89b4fa')

btn_regen_ax = plt.axes([0.55, 0.1, 0.15, 0.04])
regen_button = Button(btn_regen_ax, 'Regenerate Key', color='#a6e3a1', hovercolor='#94e2d5')

btn_eve_ax = plt.axes([0.72, 0.1, 0.18, 0.04])
eve_button = Button(btn_eve_ax, 'Toggle Eve (OFF)', color='#f38ba8', hovercolor='#eba0b2')

highlight_rect = None

def draw_grid():
    ax_grid.clear()
    
    title_str = "BB84 State Matrix - SECURE CHANNEL" if not eve_active else "BB84 State Matrix - EVE ACTIVE! (Eavesdropping)"
    title_color = '#40a02b' if not eve_active else '#d20f39'
    ax_grid.set_title(title_str, color=title_color, fontsize=13, fontweight='bold', pad=15)
    
    alice_basis_symbols = ['Z (↑)' if b == 'Z' else 'X (↗)' for b in alice_bases]
    bob_basis_symbols = ['Z (↑)' if b == 'Z' else 'X (↗)' for b in bob_bases]
    
    if eve_active:
        eve_basis_symbols = ['Z (↑)' if b == 'Z' else 'X (↗)' for b in eve_bases]
        rows = [
            ("Alice's Bits", alice_bits, '#89b4fa'),
            ("Alice's Bases", alice_basis_symbols, '#f9e2af'),
            ("Eve's Bases", eve_basis_symbols, '#f5c2e7'),
            ("Eve's Bits", eve_bits, '#cba6f7'),
            ("Bob's Bases", bob_basis_symbols, '#a6e3a1'),
            ("Bob's Measured Bits", bob_bits, '#89dceb'),
            ("Bases Match?", [("YES" if i in matching_indices else "NO") for i in range(num_bits)], '#b4befe'),
            ("Shared Key", [f"{alice_bits[i]}|{bob_bits[i]}" if i in matching_indices else "-" for i in range(num_bits)], '#fab387')
        ]
        y_start = 5.2
        y_step = 0.65
    else:
        rows = [
            ("Alice's Bits", alice_bits, '#89b4fa'),
            ("Alice's Bases", alice_basis_symbols, '#f9e2af'),
            ("Bob's Bases", bob_basis_symbols, '#a6e3a1'),
            ("Bob's Measured Bits", bob_bits, '#89dceb'),
            ("Bases Match?", [("YES" if i in matching_indices else "NO") for i in range(num_bits)], '#b4befe'),
            ("Shared Key", [str(alice_bits[i]) if i in matching_indices else "-" for i in range(num_bits)], '#fab387')
        ]
        y_start = 4.8
        y_step = 0.8
        
    ax_grid.set_xlim(-2.5, num_bits - 0.5)
    ax_grid.set_ylim(-0.5, y_start + 0.7)
    ax_grid.axis('off')
    
    for row_idx, (label, values, color) in enumerate(rows):
        y_coord = y_start - row_idx * y_step
        ax_grid.text(-2.3, y_coord, label, color='#11111b', fontsize=10, fontweight='bold', va='center', ha='right')
        
        for col_idx in range(num_bits):
            val = values[col_idx]
            is_match = col_idx in matching_indices
            
            if label == "Shared Key" and is_match:
                if alice_bits[col_idx] == bob_bits[col_idx]:
                    box_color = '#a6e3a1'
                    text_color = '#11111b'
                else:
                    box_color = '#f38ba8'
                    text_color = '#ffffff'
            elif label == "Bases Match?" and is_match:
                box_color = '#e2f4e2'
                text_color = '#40a02b'
            elif label == "Bases Match?" and not is_match:
                box_color = '#ffe3e3'
                text_color = '#d20f39'
            else:
                box_color = '#f5f5f7'
                text_color = color
                
            rect = plt.Rectangle((col_idx - 0.45, y_coord - y_step*0.38), 0.9, y_step*0.76, 
                                 facecolor=box_color, edgecolor='#cccccc', linewidth=1)
            ax_grid.add_patch(rect)
            ax_grid.text(col_idx, y_coord, str(val), color=text_color, fontsize=9, fontweight='bold', 
                        ha='center', va='center')

def draw_vector(selected_idx):
    ax_vector.clear()
    ax_vector.set_title(f"Qubit State Analysis - Bit #{selected_idx}", fontsize=14, fontweight='bold', pad=15)
    ax_vector.set_xlim(-1.5, 1.5)
    ax_vector.set_ylim(-1.6, 1.6)
    ax_vector.set_aspect('equal')
    ax_vector.axis('off')
    
    circle = plt.Circle((0, 0), 1.0, color='#cccccc', fill=False, linestyle='--', linewidth=1.5)
    ax_vector.add_patch(circle)
    
    ax_vector.axhline(0, color='#e6e6e6', linestyle=':', linewidth=1)
    ax_vector.axvline(0, color='#e6e6e6', linestyle=':', linewidth=1)
    
    alice_b = alice_bases[selected_idx]
    alice_val = alice_bits[selected_idx]
    
    if alice_b == 'Z':
        ax_vector.plot([0, 0], [-1.1, 1.1], color='#df8e1d', linestyle='-', linewidth=1.2, alpha=0.4)
        ax_vector.text(0, 1.15, "|0⟩", color='#df8e1d', fontweight='bold', ha='center')
        ax_vector.text(0, -1.25, "|1⟩", color='#df8e1d', fontweight='bold', ha='center')
        ax_x, ax_y = (0, 1) if alice_val == 0 else (0, -1)
    else:
        ax_vector.plot([-0.8, 0.8], [-0.8, 0.8], color='#df8e1d', linestyle='-', linewidth=1.2, alpha=0.4)
        ax_vector.text(0.85, 0.85, "|+⟩", color='#df8e1d', fontweight='bold', ha='center')
        ax_vector.text(-0.85, -0.95, "|-⟩", color='#df8e1d', fontweight='bold', ha='center')
        ax_x, ax_y = (1/np.sqrt(2), 1/np.sqrt(2)) if alice_val == 0 else (-1/np.sqrt(2), -1/np.sqrt(2))
        
    ax_vector.quiver(0, 0, ax_x, ax_y, angles='xy', scale_units='xy', scale=1, color='#fe640b', width=0.015, zorder=5, label="Alice's State")
    
    bob_b = bob_bases[selected_idx]
    bob_val = bob_bits[selected_idx]
    
    if bob_b == 'Z':
        bob_x, bob_y = (0, 1) if bob_val == 0 else (0, -1)
    else:
        bob_x, bob_y = (1/np.sqrt(2), 1/np.sqrt(2)) if bob_val == 0 else (-1/np.sqrt(2), -1/np.sqrt(2))
        
    if eve_active:
        eve_b = eve_bases[selected_idx]
        eve_val = eve_bits[selected_idx]
        if eve_b == 'Z':
            eve_x, eve_y = (0, 1) if eve_val == 0 else (0, -1)
        else:
            eve_x, eve_y = (1/np.sqrt(2), 1/np.sqrt(2)) if eve_val == 0 else (-1/np.sqrt(2), -1/np.sqrt(2))
            
        ax_vector.quiver(0, 0, eve_x, eve_y, angles='xy', scale_units='xy', scale=1, color='#df5b9e', width=0.012, zorder=4, label="Eve's Collapsed State")
        ax_vector.quiver(0, 0, bob_x, bob_y, angles='xy', scale_units='xy', scale=1, color='#1e66f5', width=0.009, zorder=3, label="Bob's State")
        
        is_match = selected_idx in matching_indices
        if is_match:
            if alice_val == bob_val:
                outcome_color = '#40a02b'
                explanation = f"Match! Both chose {alice_b} basis.\n" \
                              f"Eve also measured in {eve_b} basis.\n" \
                              f"No collapse error introduced.\n" \
                              f"Bits MATCH: Alice {alice_val} = Bob {bob_val}."
            else:
                outcome_color = '#d20f39'
                explanation = f"Match Mismatch! Alice/Bob chose {alice_b}.\n" \
                              f"Eve intercepted and measured in {eve_b}.\n" \
                              f"This collapsed Alice's state.\n" \
                              f"Bob got a random collapsed result!\n" \
                              f"KEY ERROR: Alice {alice_val} != Bob {bob_val}!"
        else:
            outcome_color = '#7287fd'
            explanation = f"Basis Mismatch! Alice {alice_b}, Bob {bob_b}.\n" \
                          f"Eve intercepted in {eve_b}.\n" \
                          f"Bob measured along orthogonal axis.\n" \
                          f"Bit is discarded."
    else:
        ax_vector.quiver(0, 0, bob_x, bob_y, angles='xy', scale_units='xy', scale=1, color='#1e66f5', width=0.01, zorder=4, label="Bob's State")
        
        is_match = selected_idx in matching_indices
        if is_match:
            outcome_color = '#40a02b'
            explanation = f"Match! Both chose {alice_b} basis.\n" \
                          f"Bob measured along exact same axis.\n" \
                          f"Outcome guaranteed to match Alice's bit.\n" \
                          f"Shared key bit: {alice_val}"
        else:
            outcome_color = '#d20f39'
            explanation = f"Basis Mismatch! Alice {alice_b}, Bob {bob_b}.\n" \
                          f"Bob measured along orthogonal axis.\n" \
                          f"Bit collapsed randomly and is discarded."
                          
    ax_vector.text(-1.45, -1.35, explanation, fontsize=9, color='#4c4f69', fontweight='bold',
                  bbox=dict(facecolor='#f5f5f7', edgecolor=outcome_color, boxstyle='round,pad=0.7', linewidth=2.0))
    
    ax_vector.legend(loc='upper right', fontsize=8)

def update(val):
    global highlight_rect
    selected_idx = int(bit_slider.val)
    
    if highlight_rect is not None:
        highlight_rect.remove()
        
    y_lim = 5.8 if eve_active else 5.4
    highlight_rect = plt.Rectangle((selected_idx - 0.5, -0.4), 1.0, y_lim, 
                                   facecolor='none', edgecolor='#fe640b', linewidth=2.5, linestyle='--')
    ax_grid.add_patch(highlight_rect)
    
    draw_vector(selected_idx)
    fig.canvas.draw_idle()

def on_regen(event):
    global alice_bits, alice_bases, eve_bases, eve_bits, bob_bases, bob_bits, matching_indices, shared_key_alice, shared_key_bob, highlight_rect
    alice_bits, alice_bases, eve_bases, eve_bits, bob_bases, bob_bits, matching_indices, shared_key_alice, shared_key_bob = simulate_qkd(num_bits, eve_active)
    highlight_rect = None
    draw_grid()
    bit_slider.set_val(0)
    update(0)

def on_toggle_eve(event):
    global eve_active
    eve_active = not eve_active
    if eve_active:
        eve_button.label.set_text("Toggle Eve (ON)")
        eve_button.color = '#a6e3a1'
    else:
        eve_button.label.set_text("Toggle Eve (OFF)")
        eve_button.color = '#f38ba8'
    on_regen(None)

draw_grid()
update(0)

bit_slider.on_changed(update)
regen_button.on_clicked(on_regen)
eve_button.on_clicked(on_toggle_eve)

plt.show()
