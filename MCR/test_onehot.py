cur_field = [ 12, 12, 34 ,45, 45, 12, 34, 56 ,67 ];
uniq_vals = sorted( list( set( cur_field)));
field2id = dict( [ (f,icnt) for icnt, f in enumerate( uniq_vals)]);
print( field2id);

def to_one_hot( x, field2id):
    cid = field2id[ x];
    retvec = np.zeros( len( field2id));
    retvec[ cid] = 1;
    return retvec;