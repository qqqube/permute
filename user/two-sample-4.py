from permute.stratified import sim_corr
p, rho, sim = sim_corr(x=ratings.overall, y=ratings.taidgender, group=ratings.tagender, seed = 25)
print('Test statistic:', np.round(rho, 5))
# Test statistic: 0.4459
print('P-value:', np.round(p, 5))
# P-value: 0.0901
