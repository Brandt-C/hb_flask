"""empty message

Revision ID: 1a8487dfbd97
Revises: 895e8e5faf61
Create Date: 2022-04-03 15:41:08.224340

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1a8487dfbd97'
down_revision = '895e8e5faf61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.drop_column('post', 'date_created')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('post', 'timestamp')
    # ### end Alembic commands ###