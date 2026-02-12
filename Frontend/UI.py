import customtkinter as ctk
import tkinter as tk
import math
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AnimatedOrb(ctk.CTkCanvas):
    def __init__(self, master, radius=30, **kwargs):
        super().__init__(master, width=radius*5, height=radius*5,
                         bg="#0b0f14", highlightthickness=0, **kwargs)
        self.radius = radius
        self.animation_active = True
        self.state = "listening"  # listening | thinking | speaking
        self.start_time = time.time()
        self.animate()

    def set_state(self, state):
        self.state = state

    def animate(self):
        if not self.animation_active:
            return

        self.delete("all")
        t = time.time() - self.start_time

        cx = self.winfo_width() // 2
        cy = self.winfo_height() // 2

        # State colors
        colors = {
            "listening": ("#3b8ed0", "#6aa9ff"),
            "thinking": ("#9b59b6", "#d6a2ff"),
            "speaking": ("#2ecc71", "#7dffb3")
        }

        inner, outer = colors[self.state]

        # Breathing glow
        glow = 15 * math.sin(t * 2)
        base = self.radius + glow

        # Outer halo
        for i in range(5):
            r = base + i * 6
            alpha = 0.15
            self.create_oval(
                cx-r, cy-r, cx+r, cy+r,
                fill=outer, outline=""
            )

        # Energy ripple
        wave = 10 * math.sin(t * 6)
        ripple = base + wave

        self.create_oval(
            cx-ripple, cy-ripple,
            cx+ripple, cy+ripple,
            fill=outer, outline=""
        )

        # Core orb
        self.create_oval(
            cx-base, cy-base,
            cx+base, cy+base,
            fill=inner, outline=""
        )

        self.after(30, self.animate)


class VoiceAssistantGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Kayo Assistant")
        self.geometry("260x260")
        self.resizable(False, False)
        self.overrideredirect(True)
        self.configure(bg="#0b0f14")
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.97)

        self.center_window()
        self.create_close_dot()

        self.orb = AnimatedOrb(self, radius=35)
        self.orb.pack(expand=True, pady=(25, 10))

        self.label = ctk.CTkLabel(
            self, text="Listening...",
            font=("Segoe UI", 14, "bold"),
            text_color="#cccccc"
        )
        self.label.pack(pady=(0, 15))

        # Drag window
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)

        # Demo state cycle
        self.after(2000, self.demo_states)

    def demo_states(self):
        states = [
            ("listening", "Listening..."),
            ("thinking", "Thinking..."),
            ("speaking", "Speaking...")
        ]

        def cycle(i=0):
            state, text = states[i % 3]
            self.orb.set_state(state)
            self.label.configure(text=text)
            self.after(2000, lambda: cycle(i+1))

        cycle()

    def create_close_dot(self):
        top_bar = ctk.CTkFrame(self, fg_color="#0b0f14", height=20)
        top_bar.pack(fill="x", side="top")

        close_dot = tk.Canvas(top_bar, width=14, height=14,
                              bg="#0b0f14", highlightthickness=0, cursor="hand2")
        close_dot.place(x=10, y=4)
        close_dot.create_oval(0, 0, 14, 14, fill="#FF5F56", outline="")

        close_dot.bind("<Button-1>", lambda e: self.quit())

    def center_window(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.winfo_pointerx() - self.x
        y = self.winfo_pointery() - self.y
        self.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    app = VoiceAssistantGUI()
    app.mainloop()
