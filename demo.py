import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(3)
g1=rng.normal([-1,-1],0.4,(200,2))
s=rng.normal([1.5,-0.5],0.4,(120,2))
g2m=rng.normal([-0.3,1.6],0.4,(100,2))
for pts,lab in [(g1,"G1"),(s,"S"),(g2m,"G2M")]:
    plt.scatter(pts[:,0],pts[:,1],s=12,alpha=.7,label=lab)
plt.xlabel("S-phase score");plt.ylabel("G2M score");plt.title("Cell-cycle phases (demo data)");plt.legend()
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("3 cell-cycle phases\n");print("ok")